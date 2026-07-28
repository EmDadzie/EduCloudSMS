from django.contrib import admin
from .models import ClassRoom


@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'class_teacher',
        'academic_year',
    )
