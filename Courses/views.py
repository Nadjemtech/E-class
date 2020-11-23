from django.shortcuts import render , redirect
from .models import Lesson , Course , Category
from .forms import *
from .filter import ProductFilter

# Create your views here.
def HomeView(request):
    return render(request , 'home.html')

def AboutUs(request):
    return render(request , 'about_us.html')

def ContactUs(request):
    return render(request , 'contact_us.html')

def HowStudy(request):
    return render(request , 'how_study.html')



def CoursesList(request):
    courses = Course.objects.all()
    Course_filter =ProductFilter(request.GET, queryset=courses)
    courses = Course_filter.qs
    context = {'courses': courses , 'filter':Course_filter}
    return render(request,'Courses/courses_list.html',context)


def CourseReview(request,pk):
    course = Course.objects.get(id=pk)
    context = {'course': course}
    return render(request,'Courses/course_review.html',context)


def LessonsList(request,pk):
    course = Course.objects.get(id=pk)
    lessons = course.lesson_set.all()
    context = {'lessons': lessons , 'course':course}
    return render(request,'Courses/lesson_list.html',context)


def LessonView(request,C_id,L_id):
    course = Course.objects.get(id=C_id)
    lesson = course.lesson_set.get(id=L_id)
    lessons = course.lesson_set.all()
    context = {'lesson': lesson ,'course':course,'lessons': lessons}
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


def AddLesson(request, C_id ):

    course = Course.objects.get(id= C_id )
    form = LessonForm(initial={'course_of': course})
    if request.method == 'POST':
        form = LessonForm(request.POST)
        print(form.errors)
        if form.is_valid() :
            print('DONNE DONNE')
            form.save()
            return redirect('/')
    context={'form':form,'course':course} 
            # do something.
    return render(request , 'Courses/AddLesson.html',context)
