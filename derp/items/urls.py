from django.urls import path
from .views import master_file, delete_item, new_item


app_name = 'items'

urlpatterns = [
    path('master/', master_file, name='master'),
    path('delete/<uuid:uuid>', delete_item, name='delete'),
    path('new/', new_item, name='new_item')
]
