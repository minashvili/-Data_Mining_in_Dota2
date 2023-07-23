from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Тестовые', 'слова', 'из', 'списка', 'переданного', 'в', 'рендер'],
        'outer_key1': {
            'inner_key1': 'value1',
            'inner_key2': 'value2',
            'inner_key3': 'value3'
        }
    }
    return render(request, 'main/index.html', data)


def test(request):
    return render(request, 'main/testing.html')

