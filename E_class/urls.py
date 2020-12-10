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
from django.conf.urls.static import static
from django.conf import settings
from Courses.views import *
from Student.views import *
from Teacher.views import *
urlpatterns = [
    path(r'ckeditor/',include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('', HomeView, name='Home'),
    path('course/', CoursesList, name='CoursesList'),
    path('aboutus/', AboutUs, name='AboutUs'),
    path('contactus/', ContactUs, name='ContactUs'),
    path('how_study/', HowStudy, name='HowStudy'),
    # Course_app_URL
    path('course/',include([
        path('<str:pk>/', LessonsList, name='LessonsList'),
        path('review/<str:pk>/', CourseReview, name='CourseReview'),
        path('<int:C_id>/<int:L_id>/', LessonView, name='LessonView'),
        path('add_course',AddCourseView, name='AddCourse'),
        path('update_course/<int:pk>/',UpdateCourseView, name='UpdateCourse'),
        path('<int:C_id>/add_lesson/', AddLesson, name='AddLesson'),
        path('add_lesson/Succes/', Success_Lesson, name='Success_Lesson'),
        path('add_exam/<int:E_id>', AddActivity, name='AddActivity'),
        ])),    # Student_app_URLS
    path('student/<int:S_id>',StudentInfo, name='Student_Profile'),
    path('student/update/<int:S_id>', UpdateStudent, name='Student_Update'),
    path('login/', LoginView, name='Login'),
    path('logout/', LogoutView, name='Logout'),
    path('register/', RegisterView, name='Register'),
    path('Teacher/AddTeacher', AddTeacher , name='AddTeacher'),
    path('Teacher/<int:T_id>', TeacherProfile, name='TeacherProfile'),]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

