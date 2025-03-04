from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from .models import Hotel, Geo, Room
from .forms import ReservationForm

class HotelListView(ListView):
    paginate_by = 12
    model = Hotel
    template_name = 'master.html'
    context_object_name = 'hotels'

    def get_context_data(self, **kwargs):
        context = super(HotelListView, self).get_context_data(**kwargs)
        hotels = Hotel.objects.all()
        paginator = Paginator(hotels, self.paginate_by)

        page = self.request.GET.get('page')
        hotels = paginator.get_page(page)

        context['hotels'] = hotels
        return context
    
class HotelDetailView(DetailView):
    model = Hotel
    template_name = 'hotel_detail_page.html'
    context_object_name = 'hotel'

    def get_context_data(self, **kwargs):
        context = super(HotelDetailView, self).get_context_data(**kwargs)
        hotel = self.get_object()
        geo_data = Geo.objects.filter(hotel=hotel.hotel_id).all()
        context['geo'] = geo_data
        rooms = Room.objects.filter(hotel=hotel.hotel_id).all()
        context['rooms'] = rooms
        return context

def clear_hotels(request):
    Hotel.objects.all().delete()
    if Hotel.objects.count() == 0:
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=500)
    

def hotel_detail(request, hotel_id):
    if Hotel.objects.filter(hotel_id=hotel_id).count() == 0:
        return render(request, '404.html')
    hotel = Hotel.objects.filter(hotel_id=hotel_id).values()[0]
    hotel['geo'] = Geo.objects.filter(hotel=hotel_id).values()[0]
    hotel['rooms'] = list(Room.objects.filter(hotel=hotel_id).values())
    return render(request, 'hotel_detail_page.html', {'hotel': hotel})

class ReservationFormView(CreateView):
    template_name = "reservation.html"
    form_class = ReservationForm

    def get_form_kwargs(self):
        kwargs = super(ReservationFormView, self).get_form_kwargs()
        hotel = Hotel.objects.get(hotel_id=self.kwargs['pk'])
        rooms = Room.objects.filter(hotel=hotel.hotel_id).all()
        kwargs["room"] = rooms
        return kwargs
    
    def form_valid(self, form):
        form.save()
        try:
            send_mail (
                'Reservation Confirmation',
                'Thank you for your reservation!',
                'storm@maykinmedia.nl',
                ['stormcarper@gmail.com'],
                fail_silently=False
            )
            print('Email sent')
        except:
            return HttpResponse(status=500)
        return HttpResponse(status=201)
    
def get_rooms_and_hotel(request, pk):
    if Hotel.objects.filter(hotel_id=pk).count() == 0:
        return JsonResponse({"error": "Hotel not found"}, status=404)
    hotel = Hotel.objects.get(hotel_id=pk)
    rooms = Room.objects.filter(hotel=hotel).all()
    rooms = rooms.filter(availability=True)
    return render(request, 'reservation_date.html', {'hotel': hotel, 'rooms': rooms})

def get_hotel_and_room(request, Hpk, Rpk):
    if Hotel.objects.filter(hotel_id=Hpk).count() == 0:
        return JsonResponse({"error": "Hotel not found"}, status=404)
    hotel = Hotel.objects.get(hotel_id=Hpk)
    hotel_dict = {
        'hotel_id': hotel.hotel_id,
        'name': hotel.name,
        'title': hotel.title,
        'address': hotel.address,
        'price': hotel.price,
    }
    room = Room.objects.filter(room_id=Rpk).first()
    if not room:
        return JsonResponse({"error": "Room not found"}, status=404)
    room_dict = {
        'room_id': room.room_id,
        'room_type': room.room_type,
        'price': room.price,
    }
    return JsonResponse({"hotel": hotel_dict, "room": room_dict}, status=200)






