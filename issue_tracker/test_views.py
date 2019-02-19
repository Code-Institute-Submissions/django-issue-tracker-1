from django.test import TestCase
from .models import Item


class TestViews(TestCase):

    def test_get_issues_page(self):
        page = self.client.get("/accounts/login/?next=/issues/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")
    
    def test_get_add_item_page(self):
        page = self.client.get("/issues/add")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "issue_form.html")
    
    def test_get_edit_item_page(self):
        item = Item(name="Create a Test")
        item.save()

        page = self.client.get("/issues/edit/{0}".format(item.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "issue_form.html")
    
    def test_get_edit_page_for_item_that_does_not_exist(self):
        page = self.client.get("/edit/1")
        self.assertEqual(page.status_code, 404)