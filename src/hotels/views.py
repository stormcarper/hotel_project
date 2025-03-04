from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView
from django.contrib.admin.views.decorators import staff_member_required
from .models import Hotels, Geo, Rooms

# HotelList view with automatic pagination
class HotelsListView(ListView):
    paginate_by = 12
    model = Hotels
    template_name = 'master.html'
    context_object_name = 'hotels'

    def get_context_data(self, **kwargs):
        context = super(HotelsListView, self).get_context_data(**kwargs)
        hotels = Hotels.objects.all()
        paginator = Paginator(hotels, self.paginate_by)

        page = self.request.GET.get('page')
        hotels = paginator.get_page(page)

        context['hotels'] = hotels
        return context
    
# Hotel DetailView used to view a single hotel
class HotelDetailView(DetailView):
    model = Hotels
    template_name = 'hotel_detail_page.html'
    context_object_name = 'hotel'

    def get_context_data(self, **kwargs):
        context = super(HotelDetailView, self).get_context_data(**kwargs)
        hotel = self.get_object()
        geo_data = Geo.objects.filter(hotel=hotel.hotel_id).all()
        context['geo'] = geo_data
        rooms = Rooms.objects.filter(hotel=hotel.hotel_id).all()
        context['rooms'] = rooms
        return context
