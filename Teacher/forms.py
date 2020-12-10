from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Teacher



class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2',]


class CreateTeacher(ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name','last_name','theme','degree','experience',]
