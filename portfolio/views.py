from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, template_name="portfolio/home.html", context={"projects": projects})

def pdf(request):
    return render(request, template_name="portfolio/show_resume.html")