from django.test import TestCase, Client
from hotels.models import Hotels, Geo, Rooms

class HotelViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        hotel1 = Hotels.objects.create(
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
        Rooms.objects.create(
            hotel=hotel1,
            room_type='room1',
            price=100,
            availability=False
        )

        hotel2 = Hotels.objects.create(
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
        Rooms.objects.create(
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