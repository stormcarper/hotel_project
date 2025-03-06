from django.test import TestCase, Client
from hotels.models import Hotel, Room

class HotelAndRoomAPITest(TestCase):
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
            availability=False
        )
        Room.objects.create(
            hotel=hotel1,
            room_type='room1',
            price=100,
            availability=False
        )
        Room.objects.create(
            hotel=hotel1,
            room_type='room2',
            price=150,
            availability=True
        )

    def test_get_hotel_and_room(self):
        # Save hotel and room objects as instance attributes during setUp
        self.hotel1 = Hotel.objects.get(name='Hotel1')
        self.rooms = Room.objects.filter(hotel=self.hotel1)
        self.room1 = self.rooms[0] 
        
        response = self.client.get(f"/api/hotel/{self.hotel1.hotel_id}/room/{self.room1.room_id}")
    
        self.assertEqual(response.status_code, 200)
        hotel = response.json()['hotel']
        room  = response.json()['room']
        self.assertEqual(hotel['hotel_id'], self.hotel1.hotel_id)
        self.assertEqual(hotel['name'], self.hotel1.name)
        self.assertEqual(hotel['title'], self.hotel1.title)
        self.assertEqual(hotel['address'], self.hotel1.address)
        self.assertEqual(hotel['price'], self.hotel1.price)
        self.assertEqual(room['room_id'], self.room1.room_id)
        self.assertEqual(room['room_type'], self.room1.room_type)
        self.assertEqual(room['price'], self.room1.price)

    def test_non_existing_hotel(self):
        response = self.client.get("/api/hotel/999/room/2")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['error'], "Hotel not found")

    def test_non_existing_room(self):
        self.hotel1 = Hotel.objects.get(name='Hotel1')
        response = self.client.get(f"/api/hotel/{self.hotel1.hotel_id}/room/999")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['error'], "Room not found")