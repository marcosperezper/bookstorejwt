from rest_framework import viewsets
from .models import Author, Book
from .serializers import BookSerializer, AuthorSerializer


# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer
    lookup_field = "title"


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('name')
    serializer_class = AuthorSerializer
    lookup_field = "name"
