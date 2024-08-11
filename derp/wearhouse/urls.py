# pylint: disable=invalid-name, missing-module-docstring
from django.urls import path
from . import views


app_name = 'wearhouse'

urlpatterns = [
    path('master/', views.master_file, name='master'),
]
