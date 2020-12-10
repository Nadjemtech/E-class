from django.forms import ModelForm
from .models import Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class StudentForm(ModelForm):
    """Form definition for Student."""

    class Meta:
        """Meta definition for Studentform."""

        model = Student
        fields = ('name','lastName','gender','addrass','image','age','study_year')



class CreateStudent(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','email','password1','password2']