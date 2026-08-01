from django.contrib import admin
from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):

    list_display = (
        "staff_id",
        "first_name",
        "last_name",
        "gender",
        "phone",
        "email",
        "active",
    )

    search_fields = (
        "staff_id",
        "first_name",
        "last_name",
        "phone",
        "email",
    )

    list_filter = (
        "gender",
        "active",
    )

    ordering = (
        "staff_id",
    )

    list_editable = (
        "active",
    )

    list_per_page = 20