from django.urls import path
from .views import HotelListView, clear_hotels, HotelDetailView, ReservationFormView, get_rooms_and_hotel, get_hotel_and_room

urlpatterns = [
    path('', HotelListView.as_view(), name='hotels'),
    # path('get/', get_data, name='get_data'),
    path('clear/', clear_hotels, name='clear_hotels'),
    path('hotel/<int:pk>/', HotelDetailView.as_view(), name='hotel_detail'),
    path('reservation/finish/<int:pk>', ReservationFormView.as_view(), name='reservation'),
    path('reservation/date/<int:pk>', get_rooms_and_hotel, name='reservation_date'),
    path('api/hotel/<int:Hpk>/room/<int:Rpk>', get_hotel_and_room, name='get_room_from_hotel'),
]