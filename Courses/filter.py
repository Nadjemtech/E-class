import django_filters
from django_filters import FilterSet ,CharFilter
from .models import Course


import django_filters

class ProductFilter(FilterSet):
    name = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Course
        fields = ['name', 'category','teacher','theme']