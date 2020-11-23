from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
# Create your views here.


def StudentInfo(request):
    student = Student.objects.first()
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