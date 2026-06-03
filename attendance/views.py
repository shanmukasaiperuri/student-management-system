from django.shortcuts import render, redirect
from .models import Attendance
from .forms import AttendanceForm
from django.contrib.auth.decorators import login_required

@login_required
def attendance_list(request):

    attendance = Attendance.objects.all().order_by('-date')

    return render(
        request,
        'attendance/attendance_list.html',
        {'attendance': attendance}
    )

@login_required
def add_attendance(request):

    form = AttendanceForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/attendance/')

    return render(
        request,
        'attendance/add_attendance.html',
        {'form': form}
    )