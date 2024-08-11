# pylint: disable=invalid-name, missing-module-docstring
from django.urls import path
from . import views


app_name = 'wearhouse'

urlpatterns = [
    path('master/', views.master_file, name='master'),
    path('delete/<uuid:uuid>', views.delete, name='delete'),
    path('update-inline/<uuid:uuid>', views.update_inline, name='update-inline'),
    path('inline/<uuid:uuid>', views.inline, name='inline'),
]
