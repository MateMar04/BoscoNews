from django.contrib import admin

from .models import Author
from .models import Category
from .models import New


# Register your models here.
class NewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body', 'publish_date', 'category', 'author',)
    search_fields = ('id', 'title', 'publish_date', 'category', 'author',)
    list_filter = ('id', 'title', 'publish_date', 'category', 'author',)
    list_per_page = 10


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',)
    search_fields = ('id', 'first_name', 'last_name',)
    list_filter = ('id', 'first_name', 'last_name',)
    list_per_page = 10


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',)
    search_fields = ('id', 'name', 'description',)
    list_filter = ('id', 'name', 'description',)
    list_per_page = 10


admin.site.register(New, NewAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
