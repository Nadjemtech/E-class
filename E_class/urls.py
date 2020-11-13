"""E_class URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Courses.views import CoursesList, LessonsList, CourseReview , LessonView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CoursesList, name='CoursesList'),
    path('course/<str:pk>/', LessonsList, name='LessonsList'),
    path('course/review/<str:pk>/', CourseReview, name='CourseReview'),
    path('course/<str:C_id>/<str:L_id>/', LessonView, name='LessonView'),
]
