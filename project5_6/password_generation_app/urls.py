from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="pw_home"),
    path('new_pw', views.new_pw, name='new_pw'),
]