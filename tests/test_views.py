from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


class MenuViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.item1 = Menu.objects.create(Title="Pasta", Price=12, Inventory=10)
        self.item2 = Menu.objects.create(Title="Pizza", Price=15, Inventory=5)

    def test_getall(self):
        response = self.client.get("/restaurant/menu/items/")
        items = Menu.objects.all()
        serialized = MenuSerializer(items, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serialized.data)
