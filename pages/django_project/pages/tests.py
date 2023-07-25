from django.test import SimpleTestCase
from django.urls import reverse

class HomepageTests(SimpleTestCase):

    def test_url_exists_correct_location(self):
        response= self.client.get("/home/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
    
    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")


class AboutpageTests(SimpleTestCase):

    def test_url_exists_correct_location(self):
        response= self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
    
    def test_template_name_correct(self):
        response= self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")