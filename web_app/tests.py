from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Comments, Arts


# Create your tests here.


class PageTestCase(TestCase):

    """Test every page"""

    def test_index_page(self):
        response = self.client.get(reverse('web_app:index'))
        self.assertEqual(response.status_code, 200)

    def test_contact_page(self):
        response = self.client.get(reverse('web_app:contact'))
        self.assertEqual(response.status_code, 200)

    def test_about_page(self):
        response = self.client.get(reverse('web_app:about'))
        self.assertEqual(response.status_code, 200)

    def test_register_page(self):
        response = self.client.get(reverse('web_app:register'))
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        response = self.client.get(reverse('web_app:login'))
        self.assertEqual(response.status_code, 200)

    def test_write_page(self):
        response = self.client.get(reverse('web_app:write'))
        self.assertEqual(response.status_code, 302)


class UnknownPageTestCase(TestCase):
    """Test presence of the 404 page"""

    def test_no_page(self):
        response = self.client.get('/web_app/nopage.html')
        self.assertEqual(response.status_code, 404)


class LoginTestCase(TestCase):

    """Create a fake user and test the login function"""

    def test_fake_user(self):

        self.username = "Fake"
        self.password = "User"
        self.email = "test@test.test"

        # Save the fake user
        User.objects.create_user(self.username, self.email, self.password)

    def test_log_usr(self):

        c = Client()
        response = c.post('/web_app/login/', {'username': 'Fake', 'password': 'User'})
        self.assertEqual(response.status_code, 200)


class CommentTestCase(TestCase):

    """ Create a fake commentary """

    def test_add_comment(self):
        self.comments = "Fake comments"
        self.user_id = 99
        self.art_id = 99

        com = Comments(comments=self.comments, user_id=self.user_id, art_id=self.art_id)
        com.save()


class ArtTestCase(TestCase):

    """ Create a fake article """

    def test_add_fakeArt(self):
        self.title = "Title"
        self.txt = "Lorem ipsum dolor sit amet"
        self.user_id = "99"
        self.preview = "Tema tis rolod muspi merol"
        self.date = "2019-07-29"
        self.preview = "Tema tis rolod muspi merol"

        art = Arts(title=self.title, txt=self.txt, user_id=self.user_id, date=self.date, preview=self.preview)
        art.save()








