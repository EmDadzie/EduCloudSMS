from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Administrator"
        HEADTEACHER = "HEADTEACHER", "Headteacher"
        TEACHER = "TEACHER", "Teacher"
        PARENT = "PARENT", "Parent"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.TEACHER
    )

    def __str__(self):
        return f"{self.username} ({self.role})"