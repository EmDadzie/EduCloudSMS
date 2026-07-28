from django.contrib import admin
from .models import SubjectAssignment


@admin.register(SubjectAssignment)
class SubjectAssignmentAdmin(admin.ModelAdmin):

    list_display = (
        'teacher',
        'subject',
        'class_room',
        'academic_year',
    )