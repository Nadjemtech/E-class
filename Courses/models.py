from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from embed_video.fields import EmbedVideoField


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
        db_table            = ''
        managed             = True
        verbose_name        = 'Category'
        verbose_name_plural = 'Categorys'   


class Course(models.Model):

    name            = models.CharField(max_length=100 , null=False)
    image           = models.ImageField(max_length=2000,blank=True, null=True)
    rating          = models.IntegerField(default=0)
    description     = models.TextField()
    category        = models.ForeignKey('Category',null=True, on_delete=models.SET_NULL)
    teacher         = models.CharField(max_length=300 , null=True , blank=True)
    theme           = models.CharField(max_length=100 , blank=True, null=True)



    def __str__(self):
        return self.name

    class Meta:
        db_table            = ''
        managed             = True
        verbose_name        = 'Course'
        verbose_name_plural = 'Courses'


class Lesson(models.Model):
    id              = models.AutoField(primary_key=True)
    order           = models.IntegerField(default='1',blank=True, null=True)
    lesson_name     = models.CharField(max_length=255,blank=True, null=True)
    document        = RichTextUploadingField(blank=True, null=True)
    video           = EmbedVideoField(null=True , blank=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now_add=True)
    course_of       = models.ForeignKey('Course',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.lesson_name

    
    class Meta:
        db_table            = ''
        managed             = True
        verbose_name        = 'Lesson'
        verbose_name_plural = 'Lessons'

class Examination(models.Model):
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE)
    def __str__(self):
        return 'Exam of '+self.lesson.lesson_name

    class Meta:
        db_table            = ''
        managed             = True
        verbose_name        = 'Examination'
        verbose_name_plural = 'Examinations'

class Activity(models.Model):

    question        = RichTextUploadingField(blank=True, null=True)
    exam            = models.ForeignKey('Examination',null=True, on_delete=models.CASCADE)
    image           = models.ImageField(null=True , blank=True)


    def __str__(self):
        return 'Activity'


class Choices(models.Model):
    true    = 'true'
    false   = 'false'
    TYPE    = [
                (true,'true'),
                (false,'false')
                ]

    content         = models.CharField(max_length=1000)
    type            = models.CharField(max_length=10,choices=TYPE)
    activity        = models.ForeignKey('Activity',null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.content

    class Meta:
        db_table            = ''
        managed             = True
        verbose_name        = 'Choices'
        verbose_name_plural = 'Choicess'



class Explanation(models.Model):
    explain         = RichTextUploadingField(blank=True, null=True)
    video           = EmbedVideoField(null=True , blank=True)
    activity        = models.ForeignKey('Activity',null=True, on_delete=models.CASCADE)
    
    class Meta:
        db_table            = ''
        managed             = True
        verbose_name        = 'Explanation'
        verbose_name_plural = 'Explanations'


RATE_CHOICES = [
	(1, '1 - Trash'),
	(2, '2 - Horrible'),
	(3, '3 - Terrible'),
	(4, '4 - Bad'),
	(5, '5 - OK'),
	(6, '6 - Watchable'),
	(7, '7 - Good'),
	(8, '8 - Very Good'),
	(9, '9 - Perfect'),
	(10, '10 - Master Piece'), 
]


class Review(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)
	text = models.TextField(max_length=3000, blank=True)
	rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
	like = models.BooleanField(default=0)

	def __str__(self):
		return self.user.username