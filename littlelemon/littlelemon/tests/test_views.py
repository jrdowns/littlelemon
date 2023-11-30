from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setup(self):
        self.menu_item1 = MenuItem.objects.create(title = "Pizza", price = 12.99, inventory = 5)
        self.menu_item2 = MenuItem.objects.create(title = "Burger", price = 8.99, inventory = 10)
        
    def test_getall(self):
        url = reverse('MenuItemsView') # takes a view name as an argument and returns the corresponding URL
        response = self.client.get(url) # sends a GET request to the URL returned by 'reverse' and stores the response in the 'response' variable
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        menu_items = MenuItem.objects.all() # gets a queryset of all 'Menu' objects from the database
        serializer = MenuItemSerializer(menu_items, many = True) # serializes the queryset of 'Menu' objects into a JSON-like format
        self.assertEqual(response.data, serializer.data)