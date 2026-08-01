from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = (
        "admission_number",
        "first_name",
        "last_name",
        "class_room",
        "gender",
        "parent_phone",
    )

    search_fields = (
        "admission_number",
        "first_name",
        "last_name",
        "parent_name",
        "parent_phone",
    )

    list_filter = (
        "gender",
        "class_room",
    )

    ordering = (
        "admission_number",
    )

    list_per_page = 20