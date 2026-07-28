from django.db import models
from students.models import Student
from subjects.models import Subject
from classes.models import ClassRoom


class Assessment(models.Model):

    ASSESSMENT_TYPE = [
        ("CLASSWORK", "Classwork"),
        ("HOMEWORK", "Homework"),
        ("QUIZ", "Quiz"),
        ("CA", "Continuous Assessment"),
        ("EXAM", "Examination"),
    ]

    title = models.CharField(max_length=100)

    assessment_type = models.CharField(
        max_length=20,
        choices=ASSESSMENT_TYPE
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE
    )

    class_room = models.ForeignKey(
        ClassRoom,
        on_delete=models.CASCADE
    )

    term = models.CharField(
        max_length=20
    )

    academic_year = models.CharField(
        max_length=20
    )

    total_marks = models.PositiveIntegerField(
        default=100
    )

    is_approved = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.title



class Score(models.Model):

    assessment = models.ForeignKey(
        Assessment,
        on_delete=models.CASCADE
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    score = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    submitted = models.BooleanField(
        default=False
    )


    def __str__(self):
        return f"{self.student} - {self.assessment}"
