from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("about/", views.about_page, name="about"),
    path("courses", views.courses, name="courses"),
    path("courses/<int:pk>", views.course_detail, name="course_detail"),
]
