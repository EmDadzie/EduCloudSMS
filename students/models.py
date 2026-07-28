from classes.models import ClassRoom
from django.db import models
from django.utils import timezone


class Student(models.Model):

    class Gender(models.TextChoices):
        MALE = "MALE", "Male"
        FEMALE = "FEMALE", "Female"


    class Status(models.TextChoices):
        ACTIVE = "ACTIVE", "Active"
        GRADUATED = "GRADUATED", "Graduated"
        TRANSFERRED = "TRANSFERRED", "Transferred"
        WITHDRAWN = "WITHDRAWN", "Withdrawn"


    admission_number = models.CharField(
        max_length=20,
        unique=True,
        blank=True
    )

    first_name = models.CharField(
        max_length=50
    )

    last_name = models.CharField(
        max_length=50
    )

    gender = models.CharField(
        max_length=10,
        choices=Gender.choices
    )

    date_of_birth = models.DateField()

    parent_name = models.CharField(
        max_length=100
    )

    parent_phone = models.CharField(
        max_length=15
    )

    address = models.TextField()

    photo = models.ImageField(
        upload_to="student_photos/",
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE
    )

    class_room = models.ForeignKey(
        ClassRoom,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="students"
    )

    date_registered = models.DateField(
        auto_now_add=True
    )


    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


    def save(self, *args, **kwargs):

        if not self.admission_number:

            year = timezone.now().year

            last_student = Student.objects.order_by(
                "-id"
            ).first()

            if last_student:
                number = last_student.id + 1
            else:
                number = 1

            self.admission_number = (
                f"ADB-{year}-{number:04d}"
            )

        super().save(*args, **kwargs)


    def __str__(self):
        return self.full_name
    
