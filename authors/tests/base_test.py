# django imports
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework.test import APITestCase, APIClient

# local imports
from authors.apps.authentication.activate import account_activation_token
from authors.apps.authentication.models import User


class TestBase(APITestCase):
    """This class defines the basic setup for the tests
        and the dummy data used for the tests.
    """

    def setUp(self):
        """This method is used to initialize variables used by the tests."""

        self.client = APIClient()
        self.login_url = reverse('authentication:login_url')
        self.user_url = reverse('authentication:signup_url')
        self.update_url = reverse('authentication:user_update')

        self.user_data = {
            "user": {
                "username": "sam",
                "email": "sam@gmail.com",
                "password": "A23DVFRss@"
            }}
        self.update_data = {
            "user": {
                "username": "sam2",
                "email": "sam@gmail.com",
                "password": "A23DVFRss@2"
            }}
        self.test_username = {
            "user": {
                "username": "sam",
                "email": "sam@gmail.com",
                "password": "A23DVFRss@"
            }}

        self.test_username2 = {
            "user": {
                "username": "sam",
                "email": "sly@gmail.com",
                "password": "A23DVFRss@"
            }}

        self.empty_email = {
            "user": {
                "username": "sam",
                "email": "",
                "password": "A23DVFRss@"
            }}
        self.blank_mail = {
            "email": ""
        }

        self.empty_password = {
            "user": {
                "username": "sam",
                "email": "sami@gmail.com",
                "password": ""
            }}

        self.empty_username = {
            "user": {
                "username": "",
                "email": "sami@gmail.com",
                "password": "904438283278"
            }}

        self.login_data = {
            "user": {
                "email": "sam@gmail.com",
                "password": "A23DVFRss@"
            }}

        self.test_wrong_login = {
            "user": {
                "email": "sammy@gmail.com",
                "password": "A23DVFRss@"
            }}

        self.test_empty_email = {
            "user": {
                "email": "",
                "password": "A23@"
            }}

        self.test_login_unregistered = {
            "user": {
                "email": "sammy@gmail.com",
                "password": "A23@"
            }}
        self.signup_user_data = {
            'user': {
                'username': 'Allan123',
                'email': 'cake@foo.com',
                'password': 'Yertg234D#'
            }
        }
        self.reset_password_email = {
            "email": "sam@gmail.com"
        }
        self.inexistent_email = {
            "email": "job@yahoo.com"
        }
        self.reset_password_invalid_email = {
            "email": "kenyamoja@gmail.com"
        }
        
    def get_token(self):
        """Register and login a user"""

        # register user
        self.client.post(
            self.user_url,
            self.user_data,
            format='json'
        )
        self.client.get(self.get_verify_url(self.user_data))
        response = self.client.post(
            self.login_url,
            self.login_data,
            format="json"
        )
        token = response.data['token']
        return token
        
    def get_verify_url(self, user):

        self.register_user()
        user_to_activate = User.objects.get(username=user['user']['username'])
        pk = urlsafe_base64_encode(force_bytes(user_to_activate.id)).decode()
        token = account_activation_token.make_token(user_to_activate)
        url = reverse('authentication:activate', kwargs={"pk": pk,
                                                         "token": token})
        return url

    def register_user(self, ):
        return self.client.post(
            self.user_url,
            self.user_data,
            format='json'
        )

    def register_duplicate_email(self, ):
        return self.client.post(
            self.user_url,
            self.user_data,
            format='json'
        )

    def register_duplicate_username(self, ):
        return self.client.post(
            self.user_url,
            self.test_username2,
            format='json'
        )

    def register_empty_email(self, ):
        return self.client.post(
            self.user_url,
            self.empty_email,
            format='json'
        )

    def register_empty_password(self, ):
        return self.client.post(
            self.user_url,
            self.empty_password,
            format='json'
        )

    def register_empty_username(self, ):
        return self.client.post(
            self.user_url,
            self.empty_username,
            format='json'
        )

    def login_user(self, ):
        return self.client.post(
            self.login_url,
            self.login_data,
            format="json"
        )

    def login_wrong_user_details(self, ):
        return self.client.post(
            self.login_url,
            self.test_wrong_login,
            format="json"
        )

    def login_empty_email(self, ):
        return self.client.post(
            self.login_url,
            self.test_empty_email,
            format="json"
        )
