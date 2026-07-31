from django.db import models


class School(models.Model):
    school_name = models.CharField(
        max_length=200
    )

    motto = models.CharField(
        max_length=255,
        blank=True
    )

    logo = models.ImageField(
        upload_to="school_logos/",
        blank=True,
        null=True
    )

    academic_year = models.CharField(
        max_length=20,
        default="2026/2027"
    )

    email = models.EmailField(
        blank=True
    )

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    website = models.URLField(
        blank=True
    )

    address = models.TextField(
        blank=True
    )

    primary_color = models.CharField(
        max_length=7,
        default="#0A2540"
    )

    secondary_color = models.CharField(
        max_length=7,
        default="#C9A227"
    )

    class Meta:
        verbose_name = "School"
        verbose_name_plural = "School"

    def __str__(self):
        return self.school_name