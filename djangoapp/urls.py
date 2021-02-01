from django.conf.urls import url
from . import views


app_name = "djangoapp"

urlpatterns = [
    url('', views.index, name='index'),
]