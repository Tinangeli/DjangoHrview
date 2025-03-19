from django.urls import path
from django.shortcuts import render

from . import views
from .views import *



urlpatterns = [
    path("", views.index, name="index"),
    #path("schedules/", views.schedules_view, name="schedules"),
    path('schedules/', schedule_view, name='schedule_view'),
    path('generate-summary/', views.generate_observation_summary, name='generate_summary'),

]