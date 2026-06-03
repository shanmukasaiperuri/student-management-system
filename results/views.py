from django.shortcuts import render, redirect

from .models import Result
from .forms import ResultForm
from django.contrib.auth.decorators import login_required

@login_required
def result_list(request):

    results = Result.objects.all()

    return render(
        request,
        'results/result_list.html',
        {'results': results}
    )

@login_required
def add_result(request):

    form = ResultForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/results/')

    return render(
        request,
        'results/add_result.html',
        {'form': form}
    )

@login_required
def update_result(request, pk):

    result = Result.objects.get(id=pk)

    form = ResultForm(
        request.POST or None,
        instance=result
    )

    if form.is_valid():
        form.save()
        return redirect('/results/')

    return render(
        request,
        'results/update_result.html',
        {'form': form}
    )

@login_required
def delete_result(request, pk):

    result = Result.objects.get(id=pk)

    if request.method == "POST":
        result.delete()
        return redirect('/results/')

    return render(
        request,
        'results/delete_result.html',
        {'result': result}
    )