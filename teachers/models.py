from django.db import models


class Teacher(models.Model):

    class Gender(models.TextChoices):
        MALE = "Male", "Male"
        FEMALE = "Female", "Female"

    first_name = models.CharField(max_length=50)

    last_name = models.CharField(max_length=50)

    gender = models.CharField(
        max_length=10,
        choices=Gender.choices
    )

    staff_id = models.CharField(
        max_length=20,
        unique=True
    )

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    email = models.EmailField(
        blank=True
    )

    photo = models.ImageField(
        upload_to="teacher_photos/",
        blank=True,
        null=True
    )

    date_joined = models.DateField(
        auto_now_add=True
    )

    active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"