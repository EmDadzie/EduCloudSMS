from django.shortcuts import render

from students.models import Student
from teachers.models import Teacher


def home(request):

    context = {

        "recent_students": Student.objects.order_by(
            "-date_registered"
        )[:5],

        "recent_teachers": Teacher.objects.order_by(
            "-date_joined"
        )[:5],

    }

    return render(
        request,
        "dashboard/home.html",
        context,
    )