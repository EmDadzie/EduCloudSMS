from django.db import models
from students.models import Student
from teachers.models import Teacher


class Attendance(models.Model):

    class Status(models.TextChoices):
        PRESENT = "PRESENT", "Present"
        ABSENT = "ABSENT", "Absent"
        LATE = "LATE", "Late"


    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    date = models.DateField()

    status = models.CharField(
        max_length=10,
        choices=Status.choices
    )

    recorded_by = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    class Meta:
        unique_together = (
            'student',
            'date',
        )


    def __str__(self):
        return f"{self.student} - {self.date} - {self.status}"
