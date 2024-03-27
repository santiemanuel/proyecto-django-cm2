from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("cursos/", views.curso_list, name="curso_list"),
    path("cursos/<int:curso_id>/", views.curso_detail, name="curso_detail"),
]

handler404 = "cursos.views.error_404"
