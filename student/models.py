from django.db import models

class Student(models.Model):
    name = models.CharField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=8)

    def __str__(self):
        return self.name
