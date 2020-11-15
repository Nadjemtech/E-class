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
from django.urls import path , include
from Courses.views import CoursesList, LessonsList, CourseReview , LessonView, AddCourseView ,UpdateCourseView
from Student.views import StudentInfo
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CoursesList, name='CoursesList'),
    # Course_app_URL
    path('course/',include([
        path('<str:pk>/', LessonsList, name='LessonsList'),
        path('review/<str:pk>/', CourseReview, name='CourseReview'),
        path('<int:C_id>/<int:L_id>/', LessonView, name='LessonView'),
        path('add_course',AddCourseView, name='AddCourse'),
        path('update_course/<int:pk>/',UpdateCourseView, name='UpdateCourse'),
        ])),    # Student_app_URLS
    path('student/',StudentInfo, name='Student_Profile'),
]
