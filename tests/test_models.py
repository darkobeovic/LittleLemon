from django.test import TestCase
from restaurant.models import Menu


class MenuModelTest(TestCase):

    def test_str(self):
        item = Menu.objects.create(
            Title="IceCream",
            Price=80,
            Inventory=100
        )
        self.assertEqual(str(item), "IceCream : 80")
