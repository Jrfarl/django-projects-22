from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name="data_home"),
    path('confirm_add', views.confirm_add, name='confirm_add'),
]