from django.shortcuts import render
from .models import *

def about(request):
    chart = Chart.objects.all()
    
    context = {
        "chart": chart
       
    }
    
    return render(request, 'base.html', context)
def charts(request):
    chart = Chart.objects.all()
    
    context = {
        "chart": chart
       
    }
    return render(request, 'charts.html', context)
def chart2(request):
    chart2 = Chart2.objects.all()

    context = {
        "chart2": chart2    
    }
    return render(request, 'Charts2.html', context)