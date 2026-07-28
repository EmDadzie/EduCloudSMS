from django.db import models


class School(models.Model):

    name = models.CharField(max_length=200)

    motto = models.CharField(
        max_length=255,
        blank=True
    )

    address = models.TextField(
        blank=True
    )

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    email = models.EmailField(
        blank=True
    )

    logo = models.ImageField(
        upload_to="school_logo/",
        blank=True,
        null=True
    )

    academic_year = models.CharField(
        max_length=20,
        default="2026/2027"
    )

    CURRENT_TERM = [
        ("Term 1", "Term 1"),
        ("Term 2", "Term 2"),
        ("Term 3", "Term 3"),
    ]

    current_term = models.CharField(
        max_length=10,
        choices=CURRENT_TERM,
        default="Term 1"
    )

    def __str__(self):
        return self.name
