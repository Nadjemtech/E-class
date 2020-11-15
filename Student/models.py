from django.db import models
from Courses.models import Course
# Create your models here.


class Student(models.Model):
    GENDER= [('Male','Male'),('Female','Female')]

    name = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    gender = models.CharField(max_length=100,choices=GENDER , default='Male')
    addrass = models.CharField(max_length=100,blank=True, null=True)
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