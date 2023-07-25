from django.shortcuts import render

# Create your views here.
def datamining_home(request):
    return render(request, 'datamining/datamining_home.html', {'title':'Дата майнинг'})

