from django.shortcuts import render, redirect
from django.db.models import Q

from .models import Teacher
from .forms import TeacherForm
from django.contrib.auth.decorators import login_required

@login_required
def teacher_list(request):

    search = request.GET.get('search')

    teachers = Teacher.objects.all()

    if search:
        teachers = teachers.filter(
            Q(name__icontains=search) |
            Q(email__icontains=search)
        )

    return render(
        request,
        'teachers/teacher_list.html',
        {'teachers': teachers}
    )

@login_required
def add_teacher(request):

    form = TeacherForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/teachers/')

    return render(
        request,
        'teachers/add_teacher.html',
        {'form': form}
    )

@login_required
def update_teacher(request, pk):

    teacher = Teacher.objects.get(id=pk)

    form = TeacherForm(
        request.POST or None,
        instance=teacher
    )

    if form.is_valid():
        form.save()
        return redirect('/teachers/')

    return render(
        request,
        'teachers/update_teacher.html',
        {'form': form}
    )

@login_required
def delete_teacher(request, pk):

    teacher = Teacher.objects.get(id=pk)

    if request.method == "POST":
        teacher.delete()
        return redirect('/teachers/')

    return render(
        request,
        'teachers/delete_teacher.html',
        {'teacher': teacher}
    )