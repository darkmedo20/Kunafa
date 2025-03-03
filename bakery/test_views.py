from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Menu, Drink

'''class DrinkViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Drink.objects.create(name="karak", temp="hot")
        Drink.objects.create(name="IcedCoffee", temp="cold")
        
    def test_getall(self):
        response = self.client.get('/restaurant/drink/d/')  # Adjust the URL based on your API endpoint
        self.assertEqual(response.status_code, status.HTTP_200_OK)
              
        expected_data = [
            {"id": 1, "name": "karak", "temp": "hot"},
            {"id": 2, "name": "IcedCoffee", "temp": "cold"}
        ]
        
        print(response.data, '\n')
        print(expected_data, '\n')
        
        self.assertEqual(response.data, expected_data)'''


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Menu.objects.create(Title="Pizza", Price="15.0", Inventory=3)
        Menu.objects.create(Title="Pasta", Price="10.0", Inventory=2)
        
    def test_getall(self):
        response = self.client.get('/restaurant/menu/')  # Adjust the URL based on your API endpoint
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        expected_data = [
            {"id": 2, "Title": "Pizza", "Price": "15.0", "Inventory": 3},
            {"id": 3, "Title": "Pasta", "Price": "10.0", "Inventory": 2}
        ]
        self.assertEqual(response.data, expected_data)
