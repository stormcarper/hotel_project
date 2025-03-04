from django.contrib import admin
from hotels.models import Hotel, Geo, Room, Reservation

# Geo Inline to be used in HotelsAdmin
class GeoInline(admin.TabularInline):
    model = Geo
    extra = 1

# Room Inline to be used in HotelsAdmin
class RoomsInline(admin.StackedInline):
    model = Room
    extra = 1

# ModelAdmin for Hotels
@admin.register(Hotel)
class HotelsAdmin(admin.ModelAdmin):
    # Used to show the Geo and Rooms connected to a specific hotel
    inlines = [RoomsInline, GeoInline]    
    list_display = ('title', 'name', 'address', 'activity', 'type', 'availability')
    search_fields = ('title', 'name', 'address', 'activity', 'type')
    list_filter = ('availability', 'type')

@admin.register(Reservation)
class Reservation(admin.ModelAdmin):
    list_display = ('hotel', 'room', 'price', 'start_date', 'end_date', 'first_name', 'last_name', 'email', 'address', 'zip', 'country')