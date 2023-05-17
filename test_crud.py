import requests
import pytest
import unittest
from test_utils import *

class APITestCase(unittest.TestCase):
    def setUp(self):
        print("Prepare up the test environment...\n")
        self.base_url = "https://reqres.in/api/users"
        self.create_payload = {
            "name": "morpheus",
            "job": "leader"
        }
        self.update_payload = {
            "name": "morpheus",
            "job": "leader"
        }
        self.id_users = 1

    def tearDown(self):
        print("Cleaning up the test environment...")

    def test_get_all_books(self):
        response = requests.get(self.base_url)
        assert check_get_all_users(response)

    def test_get_specifics_users(self):
        self.base_url = f"{self.base_url}/{self.id_users}"
        response = requests.get(self.base_url)
        assert check_get_specifics_users(response)

    def test_create_users(self):
        response = requests.post(self.base_url, self.create_payload)
        assert check_create_users(response)

    def test_update_users(self):
        self.base_url = f"{self.base_url}/{self.id_users}"
        response = requests.put(self.base_url, self.update_payload)
        assert check_update_users(response)

    def test_delete_users(self):
        response = requests.delete(self.base_url)
        assert check_delete_users(response)


if __name__ == '__main__':
    unittest.main()