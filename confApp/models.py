# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
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
    body = models.TextField(blank=True, null=True)
    publish_date = models.DateField(blank=True, null=True)
    category = models.ForeignKey(Category, models.DO_NOTHING, db_column='category', blank=True, null=True)
    author = models.ForeignKey(Author, models.DO_NOTHING, db_column='author', blank=True, null=True)


class Image(models.Model):
    name = models.TextField()
    description = models.TextField()
    image = models.ImageField()
    new = models.ForeignKey(New, models.DO_NOTHING)
