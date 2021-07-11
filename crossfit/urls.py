from django.urls import path

from . import views


app_name = "crossfit"

urlpatterns = [
    #path('', views.FilteredDesignedComponentListView.as_view(), name='overview'),
    path("wod_<int:pk>/", views.workout_detail, name="workout-detail"),
    path("wod_add/", views.add_workout, name="workout-add"),
]
