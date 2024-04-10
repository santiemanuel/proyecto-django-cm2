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
]

handler404 = "cursos.views.error_404"
