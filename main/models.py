from django.db import models


class Location(models.Model):
    city = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    LOC_TYPES = [
        ("G", "gym"),
        ("A", "area"),
    ]
    type = models.CharField(max_length=1, choices=LOC_TYPES, default="A")
