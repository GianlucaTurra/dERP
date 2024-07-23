from django.urls import path
from .views import master_file, delete_item, new_item, update_item


app_name = 'items'

urlpatterns = [
    path('master/', master_file, name='master'),
    path('delete/<uuid:uuid>', delete_item, name='delete'),
    path('update/<uuid:uuid>', update_item, name='update'),
    path('new/', new_item, name='new_item')
]
