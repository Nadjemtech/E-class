from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Teacher(models.Model):
    teacher = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100,)
    last_name = models.CharField(max_length=100,)
    photo = models.ImageField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    fb = models.CharField(max_length=1000,blank=True, null=True)
    theme = models.CharField(max_length=100,)
    degree = models.CharField(max_length=100,)
    experience = models.IntegerField(default=1)
    def __str__(self):
        return self.first_name+' '+self.last_name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'