from django.shortcuts import render , redirect
from .models import Lesson , Course , Category
from .forms import *

# Create your views here.
def CoursesList(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request,'Courses/courses_list.html',context)


def CourseReview(request,pk):
    course = Course.objects.get(id=pk)
    context = {'course': course}
    return render(request,'Courses/course_review.html',context)


def LessonsList(request,pk):
    course = Course.objects.get(id=pk)
    lessons = course.lesson_set.all()
    context = {'lessons': lessons}
    return render(request,'Courses/lesson_list.html',context)


def LessonView(request,C_id,L_id):
    course = Course.objects.get(id=C_id)
    lesson = course.lesson_set.get(id=L_id)
    context = {'lesson': lesson}
    return render(request,'Courses/lesson_review.html',context)


def AddCourseView(request):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)

        if form.is_valid() :
            form.save()
            return redirect('/')
    context={'form':form} 
          # do something.
    return render(request , 'Courses/AddCourse.html',context)


def UpdateCourseView(request , pk):
    course = Course.objects.get(id =pk)
    form = CourseForm( instance=course )
    if request.method == 'POST':
        form = CourseForm(request.POST , instance=course)
        if form.is_valid() :
            form.save()
            return redirect('/')

    context={'form':form} 
          # do something.
    return render(request , 'Courses/UpdateCourse.html',context)