from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

from main.models import Location


class Excercise(models.Model):
    name = models.CharField(max_length=200)


class ExcerciseDetails(models.Model):
    """
    The definition of an excercise as defined in a Workout or performed in a Session.
    """
    excercise = models.ForeignKey(Excercise, on_delete=models.PROTECT)
    magnitude = models.DecimalField(max_digits=8, decimal_places=2)
    repetitions = models.PositiveIntegerField(blank=True, null=True)

    TYPES = [
        ("D", "distance"),
        ("R", "repetitions"),
    ]
    type = models.CharField(max_length=1, choices=TYPES, default="R")

    UNITS = [
        ("K", "kg"),
        ("L", "lb"),
        ("M", "m"),
        ("N", ""),
    ]
    unit = models.CharField(max_length=1, choices=UNITS, default="N")


class Workout(models.Model):
    """
    A workout definition.
    """
    name = models.CharField(max_length=200)
    excercises = models.ManyToManyField(ExcerciseDetails)
    WORKOUT_TYPES = [
        ("A", "AMRAP"),
        ("T", "for time"),
        ("M", "max"),
    ]
    type = models.CharField(max_length=1, choices=WORKOUT_TYPES, default="T")


class Session(models.Model):
    """
    A performed workout session.
    Excercises are copied from a workout definition to allow changing default values.
    """
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    workout = models.ForeignKey(Workout, on_delete=models.PROTECT)
    excercises = models.ManyToManyField(ExcerciseDetails)
    datetime = models.DateTimeField(default=datetime.now)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
