from django.shortcuts import render, redirect
from .models import Assessment, Score
from .forms import ScoreForm


def enter_scores(request, assessment_id):

    assessment = Assessment.objects.get(
        id=assessment_id
    )

    students = assessment.class_room.students.all()


    if request.method == "POST":

        for student in students:

            score = request.POST.get(
                f"student_{student.id}"
            )

            Score.objects.update_or_create(
                assessment=assessment,
                student=student,
                defaults={
                    "score": score
                }
            )

        return redirect("dashboard")


    context = {
        "assessment": assessment,
        "students": students,
    }


    return render(
        request,
        "assessments/enter_scores.html",
        context
    )

from django.shortcuts import render
from .models import Assessment


def assessment_list(request):

    assessments = Assessment.objects.all().order_by("-created_at")

    context = {
        "assessments": assessments
    }

    return render(
        request,
        "assessments/list.html",
        context
    )