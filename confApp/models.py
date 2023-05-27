from django.db import models


class Author(models.Model):
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} "


class Category(models.Model):
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class New(models.Model):
    title = models.TextField(blank=True, null=True)
    subtitle = models.TextField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    publish_date = models.DateField(blank=True, null=True)
    category = models.ForeignKey(Category, models.DO_NOTHING, db_column='category', blank=True, null=True)
    author = models.ForeignKey(Author, models.DO_NOTHING, db_column='author', blank=True, null=True)


class Image(models.Model):
    name = models.TextField()
    image = models.ImageField(upload_to='confApp/files/news_images')
    epigraph = models.TextField()
    new = models.ForeignKey(New, models.DO_NOTHING)
