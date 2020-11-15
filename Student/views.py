from django.shortcuts import render
from .models import Student
# Create your views here.


def StudentInfo(request):
    student = Student.objects.first()
    courses = student.coursesRolling.all()
    context = {'student': student, 'courses':courses}
    return render(request , 'Student/student_profile.html',context)


# def UpdateStudent(request , S_id):