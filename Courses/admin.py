from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Examination)
admin.site.register(Activity)
admin.site.register(Choices)
admin.site.register(Explanation)
admin.site.register(Review)

