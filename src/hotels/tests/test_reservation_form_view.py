from datetime import date, timedelta
from django.forms import ValidationError
from django.test import TestCase, Client
from hotels.models import Hotel, Room, Reservation
from hotels.forms import ReservationForm

class ReservationFormViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.hotel1 = Hotel.objects.create(
            title='Title1',
            name='Hotel1',
            alt='alt1',
            address='address1',
            directions='directions1',
            phone='phone1',
            tollfree='tollfree1',
            email='email1@email1.com',
            fax='fax1',
            url='http://www.url1.com',
            hours='24',
            checkin='12:00',
            checkout='12:00',
            image='image1',
            price=100,
            content='content1',
            activity='activity1',
            type='type1',
            availability=False
        )
        self.room1 = Room.objects.create(
            hotel=self.hotel1,
            room_type='room1',
            price=100,
            availability=True
        )
        self.room2 = Room.objects.create(
            hotel=self.hotel1,
            room_type='room2',
            price=200,
            availability=False
        )
        self.form_data = {
            'hotel': self.hotel1.hotel_id,
            'room': self.room1.room_id,
            'price': '100',
            'start_date': '2025-03-19',
            'end_date': '2025-03-22',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john@example.com',
            'address': '123 Test St',
            'zip': '12345',
            'country': 'US'
        }

    def test_reservation_form_valid(self):
        form = ReservationForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    # test empty form
    def test_reservation_form_empty(self):
        form = ReservationForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 11)

    # test unavailable room
    def test_reservation_form_unavailable_room(self):
        self.form_data['room'] = self.room2.room_id
        form = ReservationForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    # test non existing hotel
    def test_non_existing_hotel(self):
        self.form_data['hotel'] = 999
        form = ReservationForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('Select a valid choice. That choice is not one of the available choices.', form.errors['hotel'])


    # test non existing room
    def test_non_existing_room(self):
        self.form_data['room'] = 999
        form = ReservationForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('Select a valid choice. That choice is not one of the available choices.', form.errors['room'])

    # test invalid email
    def test_invalid_email(self):
        self.form_data['email'] = 'john'
        form = ReservationForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('Enter a valid email address.', form.errors['email'])

    # test invalid country code
    def test_invalid_country(self):
        self.form_data['country'] = 'USA'
        form = ReservationForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('Select a valid choice. USA is not one of the available choices.', form.errors['country'])

    # test invalid dates
    def test_reservation_form_invalid_dates(self):
        #test if start date is before today's date
        self.form_data['start_date'] = '2024-03-22'
        form = ReservationForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('Start date must be after today\'s date', form.non_field_errors()[0])

        # test if end date is before start date
        self.form_data['start_date'] = '2025-03-22'
        self.form_data['end_date'] = '2025-03-19'
        form = ReservationForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('End date must be after start date', form.non_field_errors()[0])

        # test if start date is the same as end date
        self.form_data['start_date'] = '2025-03-22'
        self.form_data['end_date'] = '2025-03-22'
        form = ReservationForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('Start date and End date cannot be the same', form.non_field_errors()[0])
        
