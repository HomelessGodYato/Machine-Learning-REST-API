import requests
from unittest import TestCase

class TestGetOnePrediction(TestCase):
    def test_get_one_prediction(self):
        pk = 1
        response = requests.get(f"http://127.0.0.1:8000/api/prediction/{pk}/")
        self.assertEqual(response.status_code, 200)