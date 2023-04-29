from django.test import TestCase, Client
from django.urls import reverse  
from django.contrib.auth.models import User
from video_api.models import NewVideo
import tempfile

class TrendingPageTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        my_user = User.objects.create(username='Testuser')
        cls.post = NewVideo.objects.create(user=my_user, title="This is a test!", thumbnail=tempfile.NamedTemporaryFile(suffix=".jpg").name)

    def test_model_content(self):
        self.assertEqual(self.post.title, "This is a test!")

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/trending/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("trending"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("trending"))
        self.assertTemplateUsed(response, "trending.html")

    def test_template_content(self):
        response = self.client.get(reverse("trending"))
        self.assertNotContains(response, "Not on the page")

class HomePageTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        my_user = User.objects.create(username='Testuser')
        cls.post = NewVideo.objects.create(user=my_user, title="This is a test!", thumbnail=tempfile.NamedTemporaryFile(suffix=".jpg").name)

    def test_model_content(self):
        self.assertEqual(self.post.title, "This is a test!")

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("homepage"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("homepage"))
        self.assertTemplateUsed(response, "homepage.html")

    def test_template_content(self):
        response = self.client.get(reverse("homepage"))
        self.assertNotContains(response, "Not on the page")

class UploadPageTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        my_user = User.objects.create(username='Testuser')
        cls.post = NewVideo.objects.create(user=my_user, title="This is a test!", thumbnail=tempfile.NamedTemporaryFile(suffix=".jpg").name)

    def test_model_content(self):
        self.assertEqual(self.post.title, "This is a test!")

    def test_url_exists_at_correct_location(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get("/upload/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse("UploadVideo"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse("UploadVideo"))
        self.assertTemplateUsed(response, "upload.html")

    def test_template_content(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse("UploadVideo"))
        self.assertNotContains(response, "Not on the page")