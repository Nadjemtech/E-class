from django.shortcuts import render, redirect
from .models import Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from .forms import StudentForm , CreateStudent

# Create your views here.


def LoginView(request):
    if request.method == 'POST':
	    username = request.POST.get('username')
	    password =request.POST.get('password')

	    user = authenticate(request, username=username, password=password)

	    if user is not None:
		    login(request, user)
		    return redirect('Home')
	    else:
		    messages.info(request, 'Username OR password is incorrect')
    return render(request,'Student/login.html')


def LogoutView(request):
	logout(request)
	return redirect('Login')

def RegisterView(request):
    form = CreateStudent()
    if request.method=="POST":
        form = CreateStudent(request.POST)
        if form.is_valid() :
            form.save()
            messages.success(request,'your Profile Created')
            return redirect('Login')
    context = {'form':form}
    return render(request,'Student/register.html',context)

def StudentInfo(request,S_id):
    student = Student.objects.get(id=S_id)
    courses = student.coursesRolling.all()
    context = {'student': student, 'courses':courses}
    return render(request , 'Student/student_profile.html',context)


def UpdateStudent(request ,S_id):
    student = Student.objects.get(id=S_id)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST , instance=student)
        if form.is_valid() :
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request , 'Student/update_profile.html',context)

# def UpdateStudent(request , S_id):