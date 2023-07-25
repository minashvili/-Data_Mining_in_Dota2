from django.urls import path
from . import views


urlpatterns = [
    path('', views.datamining_home, name='datamining_home')
]

