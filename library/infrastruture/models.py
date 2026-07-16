from django.db import models

# Create your models here.
class Book(models.Model):
    __tablename__ = 'Books'

    title = models.CharField(max_length=34)
    author = models.CharField(max_length=24)
    description = models.TextField(max_length=1024)
    publication = models.CharField()
    category = models.CharField()
    stock = models.IntegerField()

    def __str__(self):
        return self.title
