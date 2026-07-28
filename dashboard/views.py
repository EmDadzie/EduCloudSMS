from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from students.models import Student
from teachers.models import Teacher
from classes.models import ClassRoom
from subjects.models import Subject


@login_required
def home(request):

    context = {
        "student_count": Student.objects.count(),
        "teacher_count": Teacher.objects.count(),
        "class_count": ClassRoom.objects.count(),
        "subject_count": Subject.objects.count(),
    }

    return render(request, "dashboard/home.html", context)