from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post

# Create your tests here.


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        testuser1 = User.objects.create_user(username="swapnil", password="daisy2021")
        testuser1.save()

        # - create blog post
        test_post = Post.objects.create(
            author=testuser1,
            title="Title created in testing",
            body="Testing content...",
        )
        test_post.save()

    def test_blog_content(self) -> None:
        post = Post.objects.get(id=1)
        athr = f"{post.author}"
        ttle = f"{post.title}"
        body = f"{post.body}"
        self.assertEqual(athr, "swapnil")
        self.assertEqual(ttle, "Title created in testing")
        self.assertEqual(body, "Testing content...")
