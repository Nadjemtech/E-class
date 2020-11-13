from django.db import models
from Courses.models import Course
# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    study_year = models.IntegerField(blank=True, null=True)
    coursesRolling = models.ManyToManyField(Course)
    def __str__(self):
        return (self.name+' '+self.lastName)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Student'
        verbose_name_plural = 'Students'