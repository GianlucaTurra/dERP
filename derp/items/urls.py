from django.urls import path
from . import views


app_name = 'items'

urlpatterns = [
    path('master/', views.master_file, name='master'),
    path('delete/<uuid:uuid>', views.delete_item, name='delete'),
    path('update/inline/<uuid:uuid>', views.update_item_inline, name='update-inline'),
    path('new/', views.new_item, name='new'),
    path('new/inline', views.new_item_inline, name='new-inline'),
    path('detail/<uuid:uuid>', views.item_detail, name='detail'),
    path('inline/<uuid:uuid>', views.inline, name='inline'),
]
