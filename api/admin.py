from django.contrib import admin
from .models import Book, Author


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    search_fields = ("title__icontains",)
    list_display = ("title", "author")


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ("name__icontains",)
    list_display = ("name",)


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
