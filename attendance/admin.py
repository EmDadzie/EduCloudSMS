from django.contrib import admin
from .models import Attendance


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):

    list_display = (
        "student",
        "date",
        "status",
    )

    search_fields = (
        "student__first_name",
        "student__last_name",
        "student__admission_number",
    )

    list_filter = (
        "status",
        "date",
    )

    ordering = (
        "-date",
    )

    list_per_page = 25