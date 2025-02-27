from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView
from .models import Hotels, Geo, Rooms
import json

# Create your views here.
def hello_world(request):
    return render(request, 'hello_world.html')

@csrf_exempt
def upload_hotels(request):
    if request.method == 'POST':
        hotels = json.loads(request.body)
        for hotel in hotels:
            hotel_instance = Hotels.objects.create(
                title=hotel['title'],
                name=hotel['name'],
                alt=hotel['alt'],
                address=hotel['address'],
                directions=hotel['directions'],
                phone=hotel['phone'],
                tollfree=hotel['tollfree'],
                email=hotel['email'],
                fax=hotel['fax'],
                url=hotel['url'],
                hours=hotel['hours'],
                checkin=hotel['checkin'],
                checkout=hotel['checkout'],
                image=hotel['image'],
                price=hotel['price'],
                content=hotel['content'],
                activity=hotel['activity'],
                type=hotel['type'],
                availability=hotel['availability']
            )
            Geo.objects.create(
                hotel=hotel_instance,
                lat=hotel['geo']['lat'],
                lon=hotel['geo']['lon']
            )
            for room in hotel['rooms']:
                Rooms.objects.create(
                    hotel=hotel_instance,
                    room_type=room['type'],
                    price=room['price'],
                    availability=room['availability']
                )
        return HttpResponse(status=201)
    else:
        return HttpResponse(status=405)

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

        try:
            hotels = paginator.page(page)
        except PageNotAnInteger:
            hotels = paginator.page(1)
        except EmptyPage:
            hotels = paginator.page(paginator.num_pages)

        context['hotels'] = hotels
        return context
    
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

def clear_hotels(request):
    Hotels.objects.all().delete()
    if Hotels.objects.count() == 0:
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=500)
    

def hotel_detail(request, hotel_id):
    if Hotels.objects.filter(hotel_id=hotel_id).count() == 0:
        return render(request, '404.html')
    hotel = Hotels.objects.filter(hotel_id=hotel_id).values()[0]
    hotel['geo'] = Geo.objects.filter(hotel=hotel_id).values()[0]
    hotel['rooms'] = list(Rooms.objects.filter(hotel=hotel_id).values())
    return render(request, 'hotel_detail_page.html', {'hotel': hotel})