from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from hrapp.models.models import *
from hrapp.models.CustomModels import *

# Create your views here.
def index(request):
    schedules = Schedules.objects.active_schedules()
    return render(request,"sample.html",{"schedules":schedules})

#def schedules_view(request):
    #schedules = Schedules.objects.active_schedules()
    #return render(request, "sample.html", {"schedules": schedules})
def schedule_view(request):
    schedules = Schedules.objects.active_schedules()
    courses = list(Courses.objects.filter(is_active=1).values_list("name", flat=True))  # Get only active courses
    print("Courses data:", courses)  # Debugging output
    return render(request, "sample.html", {"schedules": schedules, "courses": courses})