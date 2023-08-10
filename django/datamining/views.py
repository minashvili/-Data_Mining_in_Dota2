from django.shortcuts import render, redirect
from .models import ServisesInSupport
from .models import TableForForm
from .forms import TableForFormForm, ServisesInSupportForm
from django.views.generic import DetailView, UpdateView, DeleteView
# Create your views here.



class EachServiseDelete(DeleteView):
    model = ServisesInSupport
    template_name = 'datamining/simple_form_delete.html'
    success_url = '/datamimig'

class EachServiseView(DetailView):
    model = ServisesInSupport
    template_name = 'datamining/datamining_dynamic.html'
    context_object_name = 'servisesinsupport'

class EachServiseUpdate(UpdateView):
    model = ServisesInSupport
    template_name = 'datamining/simple_form.html'
    # fields = ['name', 'hero_name']
    form_class = ServisesInSupportForm


def datamining_home(request):
    all_servises = ServisesInSupport.objects.order_by('-appearance_time')
    return render(request, 'datamining/datamining_home.html', {'all_servises': all_servises})

def simple_form(request):
    error = ''
    if request.method == 'POST':
        form = ServisesInSupportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была не верной'

    form = ServisesInSupportForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'datamining/simple_form.html', data)


