from django.shortcuts import render
from .models import ServisesInSupport
# Create your views here.
def datamining_home(request):
    return render(request, 'datamining/datamining_home.html', {'title':'Дата майнинг'})

def add_server_to_foreman(request):
    data = ServisesInSupport.objects.all()
    for item in data:
        print(item)

