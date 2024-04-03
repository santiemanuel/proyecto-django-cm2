from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("cursos/", views.curso_list, name="curso_list"),
    path("cursos/<int:curso_id>/", views.curso_detail, name="curso_detail"),
    path("cursos/crear/", views.curso_create, name="curso_create"),
    path("cursos/<int:curso_id>/editar", views.curso_update, name="curso_update"),
    path("cursos/<int:curso_id>/eliminar", views.curso_delete, name="curso_delete"),
]

handler404 = "cursos.views.error_404"
