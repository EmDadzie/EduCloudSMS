from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q


from classes.models import ClassRoom
from .models import Student
from .forms import StudentForm


def student_list(request):

    students = Student.objects.select_related("class_room")

    search = request.GET.get("search")

    classroom = request.GET.get("class")

    if search:

        students = students.filter(

            Q(first_name__icontains=search) |

            Q(last_name__icontains=search) |

            Q(admission_number__icontains=search)

        )

    if classroom:

        students = students.filter(class_room_id=classroom)

    paginator = Paginator(students, 10)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    context = {

        "page_obj": page_obj,

        "classes": ClassRoom.objects.all(),

        "search": search,

        "selected_class": classroom,

    }

    return render(

        request,

        "students/student_list.html",

        context

    )


def student_create(request):

    if request.method == "POST":

        form = StudentForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()

            messages.success(request, "Student added successfully.")

            return redirect("student_list")

    else:

        form = StudentForm()

    return render(
        request,
        "students/student_form.html",
        {
            "form": form
        }
    )


def student_detail(request, pk):

    student = get_object_or_404(
        Student,
        pk=pk
    )

    return render(
        request,
        "students/student_detail.html",
        {
            "student": student
        }
    )


def student_update(request, pk):

    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":

        form = StudentForm(
            request.POST,
            request.FILES,
            instance=student
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Student information updated successfully."
            )

            return redirect("student_detail", pk=student.pk)

    else:

        form = StudentForm(instance=student)

    return render(
        request,
        "students/student_form.html",
        {
            "form": form,
            "student": student,
            "editing": True,
        },
    )


def student_delete(request, pk):

    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":

        student.delete()

        messages.success(
            request,
            "Student deleted successfully."
        )

        return redirect("student_list")

    return render(
        request,
        "students/student_confirm_delete.html",
        {
            "student": student
        }
    )