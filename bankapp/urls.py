from django.urls import path

from . import views

app_name='bankapp'
urlpatterns = [

    path('', views.demo, name='demo'),
]