from django.contrib import admin
from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        'staff_id',
        'user',
        'phone',
        'qualification',
        'date_joined'
    )
