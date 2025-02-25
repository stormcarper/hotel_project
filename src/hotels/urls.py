from django.urls import path
from .views import import_data, hello_world, get_data, import_hotel

urlpatterns = [
    path('', hello_world, name='hello_world'),
    path('get/', get_data, name='get_data')
]