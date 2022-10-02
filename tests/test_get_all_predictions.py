import requests
from unittest import TestCase

class TestGetAllPredictions(TestCase):
    def test_get_all_predictions(self):
        response = requests.get("http://127.0.0.1:8000/api/predictions/")
        self.assertEqual(response.status_code, 200)