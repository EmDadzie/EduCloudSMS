from django.contrib import admin
from .models import School


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):

    list_display = (
        "school_name",
        "academic_year",
        "phone",
        "email",
    )

    search_fields = (
        "school_name",
        "email",
        "phone",
    )

    ordering = (
        "school_name",
    )