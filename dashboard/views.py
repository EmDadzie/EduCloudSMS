from django.shortcuts import render

from students.models import Student
from teachers.models import Teacher
from classes.models import ClassRoom
from subjects.models import Subject


def home(request):

    context = {

        "total_students": Student.objects.count(),

        "total_teachers": Teacher.objects.count(),

        "total_classes": ClassRoom.objects.count(),

        "total_subjects": Subject.objects.count(),

    }

    return render(
        request,
        "dashboard/home.html",
        context
    )