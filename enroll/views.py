from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404

from enroll.forms import StudentSignUpForm, TeacherSignUpForm
from .models import Course, Enrollment, Student
from django.contrib.auth.decorators import login_required
from .decorators import student_required


def home(request):
    cursos = Course.objects.order_by('name')
    context = {
        'cursos': cursos
    }
    return render(request, 'enroll/home.html', context)


def register(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form .is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = StudentSignUpForm()

    context = {
        'form': form
    }
    return render(request, 'enroll/register.html', context)


def registerteacher(request):
    if request.method == 'POST':
        form = TeacherSignUpForm(request.POST)
        if form .is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = TeacherSignUpForm()

    context = {
        'form': form
    }
    return render(request, 'enroll/register.html', context)


@login_required
@student_required
def miscursosview(request):
    current_user = request.user
    #No hacer caso a esta mierda
    cursos = Enrollment.objects.raw(
        'select enroll_course.id, enroll_course.name, enroll_enrollment.student_id from enroll_enrollment join enroll_course on enroll_course.id = enroll_enrollment.id where enroll_enrollment.student_id=' + str(current_user.id) + ''
    ) #select enroll_enrollment.id, enroll_user.id from enroll_enrollment join enroll_user on enroll_user.id = enroll_enrollment.id where enroll_user.id=3
    context = {
        'cursos': cursos,
    }
    return render(request, 'enroll/miscursos.html', context)


@login_required
@student_required
def miscursosDitView(request, course_id):
    curso = get_object_or_404(Course, pk=course_id)
    context = {
        'curso': curso
    }
    return render(request, 'enroll/miscursosdit.html', context)


@login_required
@student_required
def detailcourseview(request, course_id):
    curso = get_object_or_404(Course, pk=course_id)
    context = {
        'curso': curso
    }
    return render(request, 'enroll/detail.html', context)
