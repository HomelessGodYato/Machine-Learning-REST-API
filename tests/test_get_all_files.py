import requests
from unittest import TestCase

class TestGetAllFiles(TestCase):
    def test_get_all_files(self):

        response = requests.get("http://127.0.0.1:8000/api/files/get_all/")
        self.assertEqual(response.status_code, 200)
