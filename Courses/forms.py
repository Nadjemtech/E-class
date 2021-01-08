from django.forms import ModelForm

from django import forms
from .models import *
class CategoryForm(ModelForm):
    """Form definition for Category."""

    class Meta:
        """Meta definition for Categoryform."""

        model = Category
        fields = ['name','description']


class CourseForm(ModelForm):
    """Form definition for Course."""

    class Meta:
        """Meta definition for Courseform."""

        model = Course
        fields = ('name','image','description','category','teacher','theme')


class LessonForm(ModelForm):
    """Form definition for Lesson."""

    class Meta:
        """Meta definition for Lessonform."""

        model = Lesson
        fields = ('order','lesson_name','document','video','course_of')

class ExamForm(ModelForm):
    class Meta:
        model = Examination
        fields = ('lesson',)

class ActivityForm(ModelForm):
    """Form definition for Activity."""

    class Meta:
        """Meta definition for Activityform."""

        model = Activity
        fields = ('question','image','exam')

class ChoicesForm(ModelForm):
    """Form definition for Choices."""

    class Meta:
        """Meta definition for Choicesform."""

        model = Choices
        fields = ('content','type')


class ExplainForm(ModelForm):
    """Form definition for Explain."""

    class Meta:
        """Meta definition for Explainform."""

        model = Explanation
        fields = ('explain','video')


class RateForm(ModelForm):
	text = forms.CharField(widget=forms.Textarea(attrs={'class': 'review-text'}), required=False)
	rate = forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(), required=True)

	class Meta:
		model = Review
		fields = ('text', 'rate','like')

