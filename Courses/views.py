from django.shortcuts import render , redirect , reverse
from .models import Lesson , Course , Category
from .forms import *
from django.forms import inlineformset_factory
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
            last = Lesson.objects.last()

            return redirect('Success_Lesson')
    context={'form':form,'course':course} 
            # do something.
    return render(request , 'Courses/AddLesson.html',context)



def Success_Lesson(request):
    ls = Lesson.objects.last()
    exam =ls.examination_set.create(lesson=ls)
    context={'lesson':ls ,'exam':exam}
    return render(request , 'Courses/AddExam.html',context)


def AddActivity(request,E_id):
    E = Examination.objects.get(id=E_id)
    activity_form = ActivityForm(initial={'exam': E})
    explanation_form = ExplainForm()
    suggestion_form1 = ChoicesForm()
    suggestion_form2 = ChoicesForm()
    suggestion_form3 = ChoicesForm()
    suggestion_form4 = ChoicesForm()
    if request.method == "POST":
        activity_form = ActivityForm(request.POST)
        explanation_form = ExplainForm(request.POST)
        suggestion_form1 = ChoicesForm(request.POST)
        suggestion_form2 = ChoicesForm(request.POST)
        suggestion_form3 = ChoicesForm(request.POST)
        suggestion_form4 = ChoicesForm(request.POST)

        if activity_form.is_valid and explanation_form.is_valid and suggestion_form1.is_valid and suggestion_form2.is_valid and suggestion_form3.is_valid and suggestion_form4.is_valid :
            print("KOKOKOKOKOKOKOKOK")
            activity = activity_form.save(False)
            explain = explanation_form.save()
            choice1 = suggestion_form1.save()
            choice2 = suggestion_form2.save()
            choice3 = suggestion_form3.save()
            choice4 = suggestion_form4.save()
            activity.explanation = explain
            activity.suggestions
            activity.suggestions
            activity.suggestions
            activity.suggestions
            activity.save()
            print(activity)

            # sugg = suggestion_form.save()
            # expl = explanation_form.save()
            # act  = activity_form.save(False)

            # act.explanation= expl
            # act.suggestions= sugg
    context={'activity_form':activity_form,
            'explanation_form':explanation_form,
            'suggestion_form1':suggestion_form1,
            'suggestion_form2':suggestion_form2,
            'suggestion_form3':suggestion_form3,
            'suggestion_form4':suggestion_form4 ,}
    return render(request, 'Courses/AddActivity.html',context)
