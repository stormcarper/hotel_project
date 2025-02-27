from django.urls import path
from .views import HotelsListView, upload_hotels, clear_hotels, hotel_detail

urlpatterns = [
    path('', HotelsListView.as_view(), name='hotels'),
    path('upload/', upload_hotels, name='upload_hotels'),
    # path('get/', get_data, name='get_data'),
    path('clear/', clear_hotels, name='clear_hotels'),
    path('hotel/<int:hotel_id>/', hotel_detail, name='hotel_detail'),

]