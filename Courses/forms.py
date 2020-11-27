from django.forms import ModelForm
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


