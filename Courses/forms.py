from django.forms import ModelForm
from .models import Category , Course , Lesson

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

