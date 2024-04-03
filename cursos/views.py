from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso, Inscripcion
from datetime import date
from .forms.curso_form import CursoForm
from django.shortcuts import redirect


def home(request):
    num_cursos = Curso.objects.filter(estado="publicado").count()
    num_estudiantes = Inscripcion.objects.values("estudiante").count()

    proximo_curso = (
        Curso.objects.filter(estado="publicado", fecha_publicacion__gt=date.today())
        .order_by("fecha_publicacion")
        .first()
    )

    cursos_destacados = Curso.objects.filter(estado="publicado", destacado=True)[:3]

    cursos_destacados_data = []
    for curso in cursos_destacados:
        curso_data = {
            "id": curso.id,
            "nombre": curso.nombre,
            "descripcion": curso.descripcion,
            "imagen": f"img/{curso.categoria.color}.png",
        }
        cursos_destacados_data.append(curso_data)

    context = {
        "num_cursos": num_cursos,
        "num_estudiantes": num_estudiantes,
        "proximo_curso": proximo_curso,
        "cursos_destacados": cursos_destacados_data,
    }

    return render(request, "curso/home.html", context)


def curso_list(request):
    cursos = Curso.objects.select_related("categoria")
    cursos_data = []
    for curso in cursos:
        curso_data = {
            "id": curso.id,
            "nombre": curso.nombre,
            "descripcion": curso.descripcion,
            "precio": curso.precio,
            "fecha_publicacion": curso.fecha_publicacion,
            "categoria": curso.categoria.nombre,
            "duracion": curso.duracion,
            "num_estudiantes": curso.estudiantes.count(),
            "imagen": f"img/{curso.categoria.color}.png",
        }
        cursos_data.append(curso_data)

    context = {"cursos": cursos_data}
    return render(request, "curso/curso_list.html", context=context)


def curso_detail(request, curso_id):
    curso = (
        Curso.objects.prefetch_related("estudiantes")
        .prefetch_related("instructor")
        .get(id=curso_id)
    )

    curso_data = {
        "id": curso.id,
        "nombre": curso.nombre,
        "descripcion": curso.descripcion,
        "precio": curso.precio,
        "fecha_publicacion": curso.fecha_publicacion,
        "categoria": curso.categoria.nombre,
        "duracion": curso.duracion,
        "num_estudiantes": curso.estudiantes.count(),
        "imagen": f"img/{curso.categoria.color}.png",
        "instructor": curso.instructor,
        "imagen_instructor": f'img/{curso.instructor.nombre.split(" ")[0]}.png',
    }
    context = {"curso": curso_data}
    return render(request, "curso/curso_detail.html", context=context)


def curso_create(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("curso_list")
    else:
        form = CursoForm()

    context = {"titulo": "Nuevo Curso", "form": form, "submit": "Crear Curso"}
    # Cambiar plantilla a curso_form_bs para ver la versión de Bootstrap
    return render(request, "curso/curso_form_bs.html", context)


def curso_update(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    if request.method == "POST":
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect("curso_list")
    else:
        form = CursoForm(instance=curso)

    context = {"titulo": "Editar Curso", "form": form, "submit": "Actualizar Curso"}
    return render(request, "curso/curso_form.html", context)


def curso_delete(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    curso.delete()
    return redirect("curso_list")


def error_404(request, exception):
    return HttpResponse("<h1>Página no encontrada</h1>", status=404)
