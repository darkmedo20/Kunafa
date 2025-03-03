from django.test import TestCase
from your_app_name.models import Menu  # Replace 'your_app_name' with the actual name of your app

class MenuTest(TestCase):
    def test_get_item(self):
        # Create an instance of the Menu model
        item = Menu.objects.create(title="IceCream", price=80)
        
        # Assert that the string representation is as expected
        self.assertEqual(str(item), "IceCream : 80")

    def test_item_price(self):
        # Create another instance of the Menu model
        item = Menu.objects.create(title="Cake", price=150)
        
        # Assert that the price is as expected
        self.assertEqual(item.price, 150)

    def test_item_title(self):
        # Create another instance of the Menu model
        item = Menu.objects.create(title="Pasta", price=120)
        
        # Assert that the title is as expected
        self.assertEqual(item.title, "Pasta")