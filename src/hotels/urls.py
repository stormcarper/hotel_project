from django.urls import path
from .views import HotelsListView, HotelDetailView

urlpatterns = [
    path('', HotelsListView.as_view(), name='hotels'),
    path('hotel/<int:pk>/', HotelDetailView.as_view(), name='hotel_detail'),
]