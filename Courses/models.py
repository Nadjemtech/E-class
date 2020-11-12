from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    FRESHMAN    = 'FR'
    SOPHOMORE   = 'SO'
    JUNIOR      = 'JR'
    SENIOR      = 'SR'
    GRADUATE    = 'GR'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (GRADUATE, 'Graduate'),
        ]


    name            = models.CharField(choices=YEAR_IN_SCHOOL_CHOICES,default=FRESHMAN, max_length=3)
    description     = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'   


class Course(models.Model):

    name = models.CharField(max_length=100 , null=False)
    image = models.ImageField(max_length=2000,blank=True, null=True)
    rating= models.IntegerField(default=0)
    description=models.TextField()
    category= models.ForeignKey('Category',null=True, on_delete=models.SET_NULL)
    teacher=models.CharField(max_length=300 , null=True , blank=True)
    theme = models.CharField(max_length=100 , blank=True, null=True)



    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


class Lesson(models.Model):
    id              =models.AutoField(primary_key=True)
    order           =models.IntegerField(default='1',blank=True, null=True)
    lesson_name     =models.CharField(max_length=255,blank=True, null=True)
    document        =RichTextField(blank=True, null=True)
    video           =models.URLField(null=True , blank=True)
    created_at      =models.DateTimeField(auto_now_add=True)
    updated_at      =models.DateTimeField(auto_now_add=True)
    course_of       =models.ForeignKey('Course',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.lesson_name

    

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'

class Activity(models.Model):
    id              =models.AutoField(primary_key=True)
    question        =RichTextField(blank=True, null=True)
    lesson          = models.ForeignKey('Lesson', on_delete=models.CASCADE)
    add             =models.FileField(null=True , blank=True)
    solution        =RichTextField(blank=True, null=True)
    explanation     = models.ForeignKey('Explanation', on_delete=models.CASCADE)
    suggestions     = models.ForeignKey('Suggestion', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.id


class Suggestion(models.Model):

    id              =models.AutoField(primary_key=True)

    Content         =RichTextField(blank=True, null=True)
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Suggestion'
        verbose_name_plural = 'Suggestions'

class Explanation(models.Model):
    id              =models.AutoField(primary_key=True)
    explain         =RichTextField(blank=True, null=True)
    document        =models.FileField(null=True , blank=True)
    video           =models.URLField(null=True , blank=True)
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Explanation'
        verbose_name_plural = 'Explanations'