from django.contrib import admin
from .models import Assessment, Score


@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "assessment_type",
        "subject",
        "class_room",
        "term",
        "academic_year",
        "is_approved",
    )

    search_fields = (
        "title",
        "subject__name",
        "class_room__name",
    )

    list_filter = (
        "assessment_type",
        "term",
        "academic_year",
        "is_approved",
    )

    ordering = (
        "-created_at",
    )

    list_per_page = 20


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):

    list_display = (
        "student",
        "assessment",
        "score",
        "submitted",
    )

    search_fields = (
        "student__first_name",
        "student__last_name",
        "student__admission_number",
    )

    list_filter = (
        "submitted",
        "assessment",
    )

    ordering = (
        "student",
    )

    list_per_page = 25