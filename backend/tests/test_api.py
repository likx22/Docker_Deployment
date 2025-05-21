import unittest

from django.test import Client, TestCase
from django.urls import reverse

from user import views as user_views
from user.models import User
from utils.jwt import encrypt_password


class APITestCase(TestCase):

    def setUp(self):
        user = User(username="testuser", password=encrypt_password(str("testuser")),
                    nickname="test", mobile="+86.123456789012", magic_number=0, url="https://baidu.com")
        user.save()
        self.client = Client()

    def test_login(self):
        pass

    def test_register(self):
        """
        Example: 使用错误信息进行注册，检查返回值为失败
        """
        data = {"username": "123", "password": "21321"}
        response = self.client.post(
            reverse(user_views.register_user),
            data=data,
            content_type="application/json"
        )
        json_data = response.json()
        self.assertEqual(json_data['message'], "Error")
        self.assertEqual(response.status_code, 500)

    def test_logout(self):
        pass


if __name__ == '__main__':
    unittest.main()
