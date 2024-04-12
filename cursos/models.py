from django.db import models
from datetime import timedelta
from django.core.exceptions import ValidationError
from tinymce.models import HTMLField


class Estudiante(models.Model):
    nombre = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(
        upload_to="estudiantes", default="estudiantes/fallback.png", blank=True
    )

    def __str__(self):
        return self.nombre


class Instructor(models.Model):
    nombre = models.CharField(max_length=100)
    bio = models.TextField()
    avatar = models.ImageField(
        upload_to="instructores", default="instructores/fallback.png", blank=True
    )

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre + " - " + self.color


def precio_positivo(value):
    if value <= 0:
        raise ValidationError("El precio debe ser un número positivo.")


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    contenido = HTMLField(default="")
    precio = models.IntegerField(validators=[precio_positivo])
    fecha_publicacion = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    duracion = models.DurationField(default=timedelta(days=0))
    estado = models.CharField(
        max_length=20,
        choices=[
            ("borrador", "Borrador"),
            ("publicado", "Publicado"),
            ("archivado", "Archivado"),
        ],
    )
    requisitos = models.TextField(blank=True)
    destacado = models.BooleanField(default=False)
    instructor = models.ForeignKey(
        Instructor, on_delete=models.SET_NULL, null=True, blank=True
    )
    estudiantes = models.ManyToManyField(Estudiante, through="Inscripcion")
    imagen = models.ImageField(
        upload_to="cursos", default="cursos/fallback.png", blank=True
    )

    def __str__(self):
        return self.nombre + " - " + str(self.fecha_publicacion)


class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ["estudiante", "curso"]

    def __str__(self):
        return self.estudiante.nombre + " - " + self.curso.nombre
