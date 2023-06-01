from django.db import models
from ckeditor.fields import RichTextField


class Author(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} "


class Category(models.Model):
    name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"


class New(models.Model):
    title = models.TextField()
    new_abstract = models.TextField()
    subtitle = models.TextField()
    body = RichTextField()
    publish_date = models.DateField()
    category = models.ForeignKey(Category, models.DO_NOTHING, db_column='category')
    author = models.ForeignKey(Author, models.DO_NOTHING, db_column='author')

    def __str__(self):
        return f"{self.title}"


class Image(models.Model):
    name = models.TextField()
    image = models.ImageField()
    epigraph = models.TextField(blank=True, null=True)
    new = models.ForeignKey(New, models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"
