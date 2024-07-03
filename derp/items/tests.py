# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring, no-member
from django.test import TestCase
from .models import Item


class NewItemTestCase(TestCase):

    def test_response(self):
        response = self.client.post("/items/new/", {"name": "robonzo", "description": "."})
        print(response)
        self.assertTrue(response.status_code == 302)

    def test_creation(self):
        before_count = Item.objects.all().count()
        self.client.post("/items/new/", {"name": "robontzo", "description": "."})
        after_count = Item.objects.all().count()
        print(before_count, after_count)
        self.assertNotEqual(before_count, after_count)
