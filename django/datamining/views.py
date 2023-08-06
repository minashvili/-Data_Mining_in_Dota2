from django.shortcuts import render
from .models import ServisesInSupport
# Create your views here.
def datamining_home(request):
    all_servises = ServisesInSupport.objects.order_by('-appearance_time')
    return render(request, 'datamining/datamining_home.html', {'all_servises': all_servises})

def simple_form(request):
    return render(request, 'datamining/simple_form.html')


