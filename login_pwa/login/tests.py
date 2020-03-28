from django.test import TestCase
from django.test import Client
# Create your tests here.

class PageAvilabilityTest(TestCase):

    def test_page_avilable(self):
        c = Client()
        s = c.get('/')
        self.assertEqual(200, s.status_code)

