import django_filters
from .models import *

class OrdersFilter(django_filters.FilterSet):
    class Meta:
        model=Orders
        fields='__all__'
        exclude=['customer','date_created']
