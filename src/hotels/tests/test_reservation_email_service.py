from django.conf import settings
from django.core import mail
from django.test import TestCase

class ReservationEmailTest(TestCase):

    def test_send_mail(self):
        mail.send_mail(
            "subject here",
            "message here",
            settings.EMAIL_HOST_USER,
            ["test@test.com"]
        )
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, "subject here")
        self.assertEqual(mail.outbox[0].body, "message here")