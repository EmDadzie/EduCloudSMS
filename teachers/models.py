from django.db import models
from django.utils import timezone


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
        unique=True,
        blank=True,
        editable=False
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

    position = models.CharField(
    max_length=50,
    blank=True
    )

    qualification = models.CharField(
        max_length=100,
        blank=True
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    address = models.TextField(
        blank=True
    )

    def save(self, *args, **kwargs):

        if not self.staff_id:

            year = str(timezone.now().year)[2:]

            last_teacher = Teacher.objects.order_by("-id").first()

            if last_teacher and last_teacher.staff_id:
                try:
                    last_number = int(last_teacher.staff_id[-4:])
                    next_number = last_number + 1
                except ValueError:
                    next_number = 1
            else:
                next_number = 1

            self.staff_id = f"STA{year}{next_number:04d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"