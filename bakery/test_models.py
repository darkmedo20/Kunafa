from django.test import TestCase
from .models import Menu

class TestMenu(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title="IceCream", Price=80.0, Inventory=3)
        #self.assertEqual(str(item), "IceCream : 80.0")