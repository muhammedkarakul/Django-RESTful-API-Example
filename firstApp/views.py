from django.shortcuts import render
from rest_framework import viewsets
from firstApp.models import Author,Book
from firstApp.serializers import AuthorSerializer,BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer