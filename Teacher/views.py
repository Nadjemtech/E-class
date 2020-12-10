from django.shortcuts import render , redirect
from .forms import CreateUserForm , CreateTeacher
from .models import *

# Create your views here.


def AddTeacher(request):
    form = CreateUserForm()
    teacherForm = CreateTeacher()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        teacherForm = CreateTeacher(request.POST)
        print("THE REQUEST PASSED !!!!")
        if form.is_valid and teacherForm.is_valid:
            print("THE FORM IS VALID !!!")
            user = form.save()
            T = teacherForm.save(commit=False)
            T.teacher = user
            T.save()
            print("Teacher Added !!!!!!")
            return redirect('Login')
        else:
            print(form.errors)
    context = {'form':form , 'teacherForm':teacherForm}
    return render(request, 'Teacher/AddTeacher.html', context)



def TeacherProfile(request , T_id):
    teacher = Teacher.objects.get(id=T_id)
    context = {'teacher':teacher}
    return render(request, 'Teacher/Profile.html', context)
