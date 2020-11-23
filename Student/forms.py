from django.forms import ModelForm
from .models import Student


class StudentForm(ModelForm):
    """Form definition for Student."""

    class Meta:
        """Meta definition for Studentform."""

        model = Student
        fields = ('name','lastName','gender','addrass','image','age','study_year')
