from django.contrib import admin
from hotels.models import Hotels, Geo, Rooms

# Register your models here.
class GeoInline(admin.TabularInline):
    model = Geo
    extra = 1

class RoomsInline(admin.StackedInline):
    model = Rooms
    extra = 1

@admin.register(Hotels)
class HotelsAdmin(admin.ModelAdmin):
    inlines = [RoomsInline, GeoInline]    
    list_display = ('title', 'name', 'address', 'activity', 'type', 'availability')
    search_fields = ('title', 'name', 'address', 'activity', 'type')
    list_filter = ('availability', 'type')