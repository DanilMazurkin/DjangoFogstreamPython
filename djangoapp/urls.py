from django.conf.urls import url
from django.urls import path, re_path
from . import views


app_name = "djangoapp"

urlpatterns = [
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('all', views.all, name='all'),
    path('good', views.good, name='good'),
    re_path('^info/[a-z]', views.info, name='info')
]