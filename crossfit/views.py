from django.shortcuts import get_object_or_404, render, redirect
from django.forms import formset_factory

from .models import *
from .forms import *


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def workout_detail(request, pk):
    details = get_object_or_404(Workout, pk=pk)

    context = {
        "details": details,
    }

    return render(request, 'crossfit/workout.html', context)


def add_workout(request):
    form = WorkoutForm(request.POST or None)
    FormSet = formset_factory(form=ExcerciseDetailForm, extra=6)
    formset = FormSet()

    if request.method == "POST":
        if form.is_valid():
            contact = form.save()

            return redirect("crossfit:workout-detail", pk=pk)

    context = {
        "form": form,
        "formset": formset,
    }

    return render(request, "crossfit/workout_form.html", context)


def add_excercise(request):
    form = ExcerciseForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            contact = form.save()

            return redirect("crossfit:workout-detail", pk=pk)

    context = {
        "form": form,
    }

    return render(request, "crossfit/generic_form.html", context)
