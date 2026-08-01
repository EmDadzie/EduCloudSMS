from core.models import School
from students.models import Student
from teachers.models import Teacher
from classes.models import ClassRoom
from subjects.models import Subject


def school_info(request):
    """
    Makes the School object available in all templates.
    """

    school = School.objects.first()

    return {
        "school": school
    }


def global_statistics(request):
    """
    Makes system statistics available in all templates.
    """

    return {
        "total_students": Student.objects.count(),
        "total_teachers": Teacher.objects.count(),
        "total_classes": ClassRoom.objects.count(),
        "total_subjects": Subject.objects.count(),
    }