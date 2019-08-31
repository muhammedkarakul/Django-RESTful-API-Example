from firstApp.models import Book, Author
from rest_framework import serializers

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Author
        fields=('name','surname','books',)

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Book
        fields=('title',)