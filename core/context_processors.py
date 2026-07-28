from .models import School


def school_info(request):
    school = School.objects.first()

    return {
        "school": school
    }