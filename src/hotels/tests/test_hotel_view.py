from django.test import TestCase, Client
from hotels.models import Hotel, Geo, Room

class HotelViewTest(TestCase):
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
        Geo.objects.create(
            hotel=hotel1,
            lat=1,
            lon=1
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
        Geo.objects.create(
            hotel=hotel2,
            lat=2,
            lon=2
        )
        Room.objects.create(
            hotel=hotel2,
            room_type='room2',
            price=200,
            availability=False
        )

    def test_hotels_list_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'master.html')
        self.assertContains(response, 'Hotel1')
        self.assertContains(response, 'Hotel2')

    def test_hotels_list_view_pagination(self):
        response = self.client.get('/?page=1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'master.html')
        self.assertContains(response, 'Hotel1')
        self.assertContains(response, 'Hotel2')

    def test_hotels_list_view_wrong_pagination(self):
        response = self.client.get('/?page=3')
        self.assertEqual(response.status_code, 404)

    def test_hotels_list_view_not_integer(self):
        response = self.client.get('/?page=string')
        self.assertEqual(response.status_code, 404)

    # test hotel detail view
    def test_hotel_detail_view(self):
        hotel1 = Hotel.objects.get(title='Title1')
        response = self.client.get(f'/hotel/{hotel1.hotel_id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hotel_detail_page.html')
        self.assertContains(response, 'Title1')
        self.assertContains(response, 'image1')
        self.assertContains(response, 'content1')
        self.assertContains(response, 'address1')
        self.assertContains(response, 'room1')
        self.assertContains(response, 'room2')
        self.assertContains(response, 100)
        self.assertContains(response, 150)
        self.assertContains(response, 'Not Available')
        self.assertContains(response, 'Available')

    def test_hotel_detail_view_wrong_id(self):
        response = self.client.get('/hotel/3/')
        self.assertEqual(response.status_code, 404)

    def test_hotel_detail_view_not_integer(self):
        response = self.client.get('/hotel/string/')
        self.assertEqual(response.status_code, 404)

    def test_hotel_detail_view_rooms(self):
        hotel2 = Hotel.objects.get(title='Title2')
        response = self.client.get(f'/hotel/{hotel2.hotel_id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hotel_detail_page.html')
        self.assertContains(response, 'room2')
        self.assertContains(response, 200)
        self.assertContains(response, 'Not Available')

    

    

