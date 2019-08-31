from django.db import models

class Book(models.Model):
    title=models.CharField(max_length=70)

    def __str__(self):
        return  self.title

class Author(models.Model):
    name=models.CharField(max_length=30)
    surname=models.CharField(max_length=30)
    books=models.ManyToManyField(Book)

    def __str__(self):
        return '%s %s'%(self.name, self.surname)