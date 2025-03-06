from django.test import TestCase, Client
from hotels.models import Hotel, Room

class RoomsAndHotelAPITest(TestCase):
    def setUp(self):
        self.client = Client()
        hotel1 = Hotel.objects.create(
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
            availability=True
        )
        Room.objects.create(
            hotel=hotel1,
            room_type='room1',
            price=100,
            availability=True
        )
        Room.objects.create(
            hotel=hotel1,
            room_type='room2',
            price=150,
            availability=False
        )

        hotel2 = Hotel.objects.create(
            title='Title2',
            name='Hotel2',
            alt='alt2',
            address='address2',
            directions='directions2',
            phone='phone2',
            tollfree='tollfree2',
            email='email2@email.com',
            fax='fax2',
            url='http://www.url2.com',
            hours='24',
            checkin='12:00',
            checkout='12:00',
            image='image2',
            price=200,
            content='content2',
            activity='activity2',
            type='type2',
            availability=False
        )
        Room.objects.create(
            hotel=hotel2,
            room_type='room2',
            price=200,
            availability=False
        )

    # test to get the correct room and hotel
    def test_get_room_and_hotel(self):
        self.hotel1 = Hotel.objects.get(name='Hotel1')
        self.rooms = Room.objects.filter(hotel=self.hotel1)
        self.room1 = self.rooms[0]
        
        response = self.client.get(f"/reservation/date/{self.hotel1.hotel_id}/{self.room1.room_id}")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reservation_date.html')
        self.assertContains(response, self.hotel1.name)
        self.assertContains(response, self.room1.room_type)

    # test for a non existing hotel
    def test_non_existing_hotel(self):
        response = self.client.get(f"/reservation/date/999/999")
        self.assertTemplateUsed(response, '404.html')
        self.assertContains(response, 'Hotel not found')

    # test for a non existing room
    def test_non_existing_room(self):
        self.hotel1 = Hotel.objects.get(name='Hotel1')
        response = self.client.get(f"/reservation/date/{self.hotel1.hotel_id}/999")
        self.assertTemplateUsed(response, '404.html')
        self.assertContains(response, 'Room not found')

    # test for a unavailable room
    def test_unavailable_room(self):
        self.hotel1 = Hotel.objects.get(name='Hotel1')
        self.rooms = Room.objects.filter(hotel=self.hotel1)
        self.room2 = self.rooms[1]

        response = self.client.get(f"/reservation/date/{self.hotel1.hotel_id}/{self.room2.room_id}")
        self.assertTemplateUsed(response, '404.html')
        self.assertContains(response, 'Room not available')

    # test if room doesn't belongs to the hotel
    def test_room_does_not_belong_to_hotel(self):
        self.hotel1 = Hotel.objects.get(name='Hotel1')
        self.hotel2 = Hotel.objects.get(name='Hotel2')
        self.rooms = Room.objects.filter(hotel=self.hotel1)
        self.room1 = self.rooms[0]

        response = self.client.get(f"/reservation/date/{self.hotel2.hotel_id}/{self.room1.room_id}")
        self.assertTemplateUsed(response, '404.html')
        self.assertContains(response, 'Room does not belong to the hotel')
        