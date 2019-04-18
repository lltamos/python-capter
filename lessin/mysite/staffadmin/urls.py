from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('staff', views.staff, name='staff'),
    path('template', views.template, name='template'),
    path('form_get', views.form_get, name='form_get'),
    path('form_post', views.form_post, name='form_post'),
    path('result', views.result, name='result')
]
