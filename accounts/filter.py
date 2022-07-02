import django_filters
from .models import *
from django_filters import DateFilter

class OrderFilter(django_filters.FilterSet):
     start_date=DateFilter(field_name='created_at',lookup_expr="gte")
     end_date = DateFilter(field_name='created_at',lookup_expr='lte')
     class Meta:
        model=Order 
        fields="__all__"
        exclude=['customer','created_at']
        