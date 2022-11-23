from django.test import TestCase
from django.shortcuts import reverse

# Create your tests here.


class PagesTest(TestCase):
    def test_home_page_url(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_home_page_with_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_contain(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, "Home Page")

    def test_aboutus_url(self):
        response = self.client.get('/aboutus/')
        self.assertEqual(response.status_code, 200)

    def test_aboutus_page_with_name(self):
        response = self.client.get(reverse('aboutus'))
        self.assertEqual(response.status_code, 200)

    def test_aboutus_page_contain(self):
        response = self.client.get(reverse('aboutus'))
        self.assertContains(response, "About Us")
