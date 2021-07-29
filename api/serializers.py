from rest_framework import serializers
from .models import Book, Author
from django.contrib.auth.models import User


class BookSerializer(serializers.ModelSerializer):
    added_by = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    author = serializers.SlugRelatedField(queryset=Author.objects.all(), slug_field='name')

    class Meta:
        model = Book
        fields = ['title', 'description', 'author', 'created_date', 'added_by']


class AuthorSerializer(serializers.ModelSerializer):
    added_by = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = Author
        fields = ['name', 'created_date', 'added_by']
