from .models import School
from students.models import Student
from teachers.models import Teacher
from classes.models import ClassRoom

def school_info(request):

    school = School.objects.first()

    return {

        "school": school,

        "sidebar_students": Student.objects.count(),

        "sidebar_teachers": Teacher.objects.count(),

        "sidebar_classes": ClassRoom.objects.count(),
    }