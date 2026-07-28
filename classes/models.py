from django.db import models
from teachers.models import Teacher


class ClassRoom(models.Model):

    name = models.CharField(
        max_length=50,
        unique=True
    )

    class_teacher = models.OneToOneField(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    academic_year = models.CharField(
        max_length=20
    )

    def __str__(self):
        return self.name