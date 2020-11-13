from django.shortcuts import render
from .models import Lesson , Course , Category

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
