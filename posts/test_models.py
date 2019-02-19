from django.test import TestCase
from .models import Post


class TestPostModel(TestCase):

    
    def tes_can_create_a_post(self):
        post = Post(content="Create a Test")
        post = Post(title="Create a Test")
        post = Post(tag="Create a Test")
        post = Post(image="Create a Test")
        post.save()
        self.assertEqual(post.content, "Create a Test")
