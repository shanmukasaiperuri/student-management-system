from django.shortcuts import render, redirect
from django.db.models import Q

from .models import Student
from .forms import StudentForm

from courses.models import Course
from teachers.models import Teacher
from attendance.models import Attendance
from results.models import Result

from django.contrib.auth.decorators import login_required

@login_required
def home(request):

    search = request.GET.get('search')

    students = Student.objects.all()

    if search:
        students = students.filter(
            Q(first_name__icontains=search) |
            Q(last_name__icontains=search) |
            Q(email__icontains=search)
        )

    context = {
        'students': students,

        'student_count': Student.objects.count(),
        'course_count': Course.objects.count(),
        'teacher_count': Teacher.objects.count(),
        'attendance_count': Attendance.objects.count(),
        'result_count': Result.objects.count(),
    }

    return render(
        request,
        'home.html',
        context
    )

    search = request.GET.get('search')

    students = Student.objects.all()

    if search:
        students = students.filter(
            Q(first_name__icontains=search) |
            Q(last_name__icontains=search) |
            Q(email__icontains=search)
        )

    context = {
        'students': students,
        'student_count': students.count()
    }

    return render(request, 'home.html', context)

@login_required
def add_student(request):

    form = StudentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/')

    return render(
        request,
        'students/add_student.html',
        {'form': form}
    )

@login_required
def update_student(request, pk):

    student = Student.objects.get(id=pk)

    form = StudentForm(
        request.POST or None,
        instance=student
    )

    if form.is_valid():
        form.save()
        return redirect('/')

    return render(
        request,
        'students/update_student.html',
        {'form': form}
    )

@login_required
def delete_student(request, pk):

    student = Student.objects.get(id=pk)

    if request.method == "POST":
        student.delete()
        return redirect('/')

    return render(
        request,
        'students/delete_student.html',
        {'student': student}
    )