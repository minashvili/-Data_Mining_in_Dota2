from django.urls import path
from . import views


urlpatterns = [
    path('', views.datamining_home, name='datamining_home'),
    path('simple_form', views.simple_form, name='simple_form'),
    path('<int:pk>', views.EachServiseView.as_view(), name='dynamic_services'),
    path('<int:pk>/update', views.EachServiseUpdate.as_view(), name='services_update'),
    path('<int:pk>/delete', views.EachServiseDelete.as_view(), name='services_delete'),
]




