from django.urls import path
from .views import get_data, upload_hotels, clear_hotels, hotel_detail

urlpatterns = [
    path('', get_data, name='hotel_project'),
    path('upload/', upload_hotels, name='upload_hotels'),
    path('get/', get_data, name='get_data'),
    path('clear/', clear_hotels, name='clear_hotels'),
    path('hotel/<int:hotel_id>/', hotel_detail, name='hotel_detail'),

]