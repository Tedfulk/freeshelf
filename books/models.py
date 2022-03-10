from multiprocessing import AuthenticationError
from unicodedata import category
from urllib.error import URLError
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    URL = models.URLField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField("Category", related_name="books")
    favorited = models.ManyToManyField(User, related_name="favorite_book")

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=75)
    slug = models.SlugField(max_length=75, blank=True, unique=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Category name={self.name}>"

    def save(self):
        self.slug = slugify(self.name)
        super().save()
