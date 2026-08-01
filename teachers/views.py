from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)

from django.contrib import messages

from django.core.paginator import Paginator

from django.db.models import Q

from .models import Teacher

from .forms import TeacherForm


def teacher_list(request):

    teachers = Teacher.objects.all()

    search = request.GET.get("search")

    if search:

        teachers = teachers.filter(

            Q(first_name__icontains=search)

            | Q(last_name__icontains=search)

            | Q(staff_id__icontains=search)

            | Q(phone__icontains=search)

        )

    paginator = Paginator(teachers, 10)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "teachers/teacher_list.html",
        {
            "page_obj": page_obj,
            "search": search,
        },
    )


def teacher_create(request):

    if request.method == "POST":

        form = TeacherForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Teacher added successfully."
            )

            return redirect("teacher_list")

    else:

        form = TeacherForm()

    return render(
        request,
        "teachers/teacher_form.html",
        {
            "form": form,
        },
    )


def teacher_detail(request, pk):

    teacher = get_object_or_404(
        Teacher,
        pk=pk
    )

    return render(
        request,
        "teachers/teacher_detail.html",
        {
            "teacher": teacher,
        },
    )


def teacher_update(request, pk):

    teacher = get_object_or_404(
        Teacher,
        pk=pk
    )

    if request.method == "POST":

        form = TeacherForm(
            request.POST,
            request.FILES,
            instance=teacher,
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Teacher updated successfully."
            )

            return redirect(
                "teacher_detail",
                pk=teacher.pk,
            )

    else:

        form = TeacherForm(
            instance=teacher
        )

    return render(
        request,
        "teachers/teacher_form.html",
        {
            "form": form,
            "editing": True,
        },
    )


def teacher_delete(request, pk):

    teacher = get_object_or_404(
        Teacher,
        pk=pk
    )

    if request.method == "POST":

        teacher.delete()

        messages.success(
            request,
            "Teacher deleted successfully."
        )

        return redirect("teacher_list")

    return render(
        request,
        "teachers/teacher_confirm_delete.html",
        {
            "teacher": teacher,
        },
    )