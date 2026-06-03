from django.shortcuts import render, redirect
from django.db.models import Q

from .models import Course
from .forms import CourseForm
from django.contrib.auth.decorators import login_required

@login_required
def course_list(request):

    search = request.GET.get('search')

    courses = Course.objects.all()

    if search:
        courses = courses.filter(
            Q(course_name__icontains=search) |
            Q(course_code__icontains=search)
        )

    return render(
        request,
        'courses/course_list.html',
        {'courses': courses}
    )

@login_required
def add_course(request):

    form = CourseForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/courses/')

    return render(
        request,
        'courses/add_course.html',
        {'form': form}
    )

@login_required
def update_course(request, pk):

    course = Course.objects.get(id=pk)

    form = CourseForm(
        request.POST or None,
        instance=course
    )

    if form.is_valid():
        form.save()
        return redirect('/courses/')

    return render(
        request,
        'courses/update_course.html',
        {'form': form}
    )

@login_required
def delete_course(request, pk):

    course = Course.objects.get(id=pk)

    if request.method == "POST":
        course.delete()
        return redirect('/courses/')

    return render(
        request,
        'courses/delete_course.html',
        {'course': course}
    )