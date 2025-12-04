from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Student(models.Model):
    name = models.CharField()
    email = models.EmailField(unique=True)
    password = models.CharField()

    def set_password(self,raw_password):
        self.password = make_password(raw_password)
        self.save()

    def check_password(self,raw_password):
        return check_password(raw_password,self.password)    

    def __str__(self):
        return self.name
