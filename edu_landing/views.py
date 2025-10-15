from django.shortcuts import render, get_object_or_404
from .models import SiteSettings, HomePageContent, AboutPageContent, Course, HomePageTexts

# Create your views here.

def home_page(request):
    site_settings = SiteSettings.objects.first()
    home_texts = HomePageContent.objects.first()
    texts = HomePageTexts.objects.all()
    courses = Course.objects.all()[:3]

    context = {
        "site_settings":site_settings,
        "home_texts":home_texts,
        "texts":texts,
        "courses":courses,
    }

    return render(request, "edu_landing/home.html", context)

def about_page(request):
    site_settings = SiteSettings.objects.first()
    about_texts = AboutPageContent.objects.all()

    context = {
        "site_settings":site_settings,
        "about_texts":about_texts,
    }

    return render(request, "edu_landing/about.html", context)

def courses(request):
    site_settings = SiteSettings.objects.first()
    course = Course.objects.all()

    context = {
        "site_settings":site_settings,
        "courses":course,
    }

    return render(request, "edu_landing/courses.html", context)

def course_detail(request, pk):
    site_settings = SiteSettings.objects.first()
    course = get_object_or_404(Course, pk=pk)

    context = {
        "site_settings":site_settings,
        "course":course,
    }

    return render(request, "edu_landing/course_detail.html", context)