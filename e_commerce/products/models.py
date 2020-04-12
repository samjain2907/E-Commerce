from django.db import models

# Create your models here.
class Product(models.Model):
    image = models.ImageField(upload_to='Images/', default='Images/no-image')
    title = models.TextField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.title