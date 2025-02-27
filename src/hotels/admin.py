from django.contrib import admin
from hotels.models import Hotels, Geo, Rooms

# Geo Inline to be used in HotelsAdmin
class GeoInline(admin.TabularInline):
    model = Geo
    extra = 1

# Room Inline to be used in HotelsAdmin
class RoomsInline(admin.StackedInline):
    model = Rooms
    extra = 1

# ModelAdmin for Hotels
@admin.register(Hotels)
class HotelsAdmin(admin.ModelAdmin):
    # Used to show the Geo and Rooms connected to a specific hotel
    inlines = [RoomsInline, GeoInline]    
    list_display = ('title', 'name', 'address', 'activity', 'type', 'availability')
    search_fields = ('title', 'name', 'address', 'activity', 'type')
    list_filter = ('availability', 'type')