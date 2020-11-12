from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Lesson)
admin.site.register(Activity)
admin.site.register(Suggestion)
admin.site.register(Explanation)
admin.site.register(Course)
admin.site.register(Category)