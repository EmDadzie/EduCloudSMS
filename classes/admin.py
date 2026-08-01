from django.contrib import admin
from .models import ClassRoom


@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "class_teacher",
        "academic_year",
    )

    search_fields = (
        "name",
        "academic_year",
    )

    list_filter = (
        "academic_year",
    )

    ordering = (
        "name",
    )

    list_per_page = 20