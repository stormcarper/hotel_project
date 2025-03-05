import datetime
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

    def clean(self):
        # get the cleaned data
        cleaned_data = super().clean()
        date = datetime.date.today()
        # get the start and end date
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        room = cleaned_data.get("room")
        # check if dates are valid
        if start_date and end_date:
            if start_date > end_date:
                raise forms.ValidationError("End date must be after start date")
            if start_date < date:
                raise forms.ValidationError("Start date must be after today's date")
            if start_date == end_date:
                raise forms.ValidationError("Start date and End date cannot be the same")
        return cleaned_data
