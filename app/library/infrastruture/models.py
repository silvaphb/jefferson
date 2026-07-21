from django.db import models
from uuid import uuid4

# Create your models here.
class Book(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    title = models.CharField(max_length=34)
    author = models.CharField(max_length=24)
    description = models.TextField(max_length=1024)
    publication = models.CharField()
    category = models.CharField()
    stock = models.IntegerField()

    class Meta:
        db_table = 'book'
