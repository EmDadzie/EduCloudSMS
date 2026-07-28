from django.db import models
from teachers.models import Teacher
from subjects.models import Subject
from classes.models import ClassRoom


class SubjectAssignment(models.Model):

    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE
    )

    class_room = models.ForeignKey(
        ClassRoom,
        on_delete=models.CASCADE
    )

    academic_year = models.CharField(
        max_length=20
    )

    def __str__(self):
        return f"{self.teacher} - {self.subject} - {self.class_room}"
