from django.urls import path
from .views import *

urlpatterns = [
     path('', about),
     path('charts/', charts),
     path('chart2/', chart2)
]