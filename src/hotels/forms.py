from django import forms
from .models import Reservation, Room
from django_countries.widgets import CountrySelectWidget

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["hotel", "room", "price", "start_date", "end_date", "first_name", "last_name", "email", "address", "zip", "country"]
        widgets = {"country": CountrySelectWidget(), "start_date": forms.DateInput(attrs={"type": "date"}), "end_date": forms.DateInput(attrs={"type": "date"})}

    def __init__(self, *args, **kwargs):
        rooms = kwargs.pop("room", None)  
        
        super(ReservationForm, self).__init__(*args, **kwargs)
        if rooms:
            self.fields["room"].queryset = rooms.filter(availability=True)
            # see the room_type in the select form
            self.fields["room"].label_from_instance = lambda obj: obj.room_type
        else:
            self.fields["room"].queryset = Room.objects.filter(availability=True)

