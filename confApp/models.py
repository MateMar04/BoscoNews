from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.TextField(),
    description = models.TextField()


class Author(models.Model):
    first_name = models.TextField(),
    last_name = models.TextField()


class New(models.Model):
    title = models.TextField(),
    body = models.TextField(),
    publish_date = models.DateField(),
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
