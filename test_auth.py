import requests
import pytest
import unittest
from test_utils import *

class APITestCase(unittest.TestCase):
    def setUp(self):
        print("Prepare up the test environment...\n")
        self.base_url_register = 'https://reqres.in/api/register'
        self.base_url_login = 'https://reqres.in/api/login'
        self.valid_payload = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
        self.invalid_payload = {
            "email" : "example@mail.com"
        }
        self.max_login_attempts = 3

    def tearDown(self):
        print("Cleaning up the test environment...")

    def test_register_success(self):
        response = requests.post(self.base_url_register, json=self.valid_payload)
        assert check_register_success(response)

    def test_register_failure(self):
        response = requests.post(self.base_url_register, json=self.invalid_payload)
        assert check_register_failure(response)

    def test_login_success(self):
        response = requests.post(self.base_url_login, json=self.valid_payload)
        assert check_login_success(response)

    def test_login_failure(self):
        response = requests.post(self.base_url_login, json=self.invalid_payload)
        assert check_login_failure(response)

    @pytest.mark.skip("Skip this test for now")
    def test_login_failure_3_attempts(self):
        for _ in range(self.max_login_attempts):
            response = requests.post(self.base_url_login, json=self.invalid_payload)
        assert check_login_failure_3_attempts(response)

if __name__ == '__main__':
    unittest.main()