from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("cursos/", views.curso_list, name="curso_list"),
    path("cursos/archivados/", views.curso_list_archive, name="curso_list_archive"),
    path("cursos/<int:curso_id>/", views.curso_detail, name="curso_detail"),
    path("cursos/crear/", views.curso_create, name="curso_create"),
    path("cursos/<int:curso_id>/editar", views.curso_update, name="curso_update"),
    path("cursos/<int:curso_id>/eliminar", views.curso_delete, name="curso_delete"),
    path("cursos/<int:curso_id>/archivar", views.curso_archive, name="curso_archive"),
    path("cursos/<int:curso_id>/restaurar", views.curso_restore, name="curso_restore"),
    path(
        "cursos/<int:curso_id>/inscribir/",
        views.inscribir_alumno,
        name="inscribir_alumno",
    ),
    # Urls de estudiantes
    path("estudiantes/", views.estudiante_list, name="estudiante_list"),
    path(
        "estudiantes/<int:estudiante_id>/",
        views.estudiante_detail,
        name="estudiante_detail",
    ),
    path("estudiantes/crear/", views.create_estudiante, name="create_estudiante"),
    path(
        "estudiantes/<int:estudiante_id>/editar",
        views.update_estudiante,
        name="update_estudiante",
    ),
]

handler404 = "cursos.views.error_404"
