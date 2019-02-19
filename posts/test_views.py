from django.test import TestCase
from .models import Post

class TestViews(TestCase):

    def test_posts_page(self):
        page = self.client.get("/accounts/login/?next=/posts/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")
    
    def test_post_detail_page(self):
        page = self.client.get("posts/{0}/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "postdetail.html")
        
    def test_get_new_post_page(self):
        page = self.client.get("posts/new")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "blogpostform.html")
    
    def test_get_edit_post_page(self):
        post = Post(name="Create a Test")
        post.save()

        page = self.client.get("posts/{0}/edit".format(post.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "blogpostform.html")
    
    def test_get_edit_page_for_post_that_does_not_exist(self):
        page = self.client.get("posts/7/edit/")
        self.assertEqual(page.status_code, 404)