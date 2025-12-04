from django.db import models

class Products(models.Model):
    name = models.CharField()
    image = models.CharField()
    price = models.IntegerField()

    def __str__(self):
        return self.name
