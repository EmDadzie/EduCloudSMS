from django.db import models
from accounts.models import User


class Teacher(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'TEACHER'}
    )

    staff_id = models.CharField(
        max_length=20,
        unique=True
    )

    phone = models.CharField(
        max_length=15
    )

    qualification = models.CharField(
        max_length=100
    )

    date_joined = models.DateField(
        auto_now_add=True
    )

    def __str__(self):
        return self.user.get_full_name()
