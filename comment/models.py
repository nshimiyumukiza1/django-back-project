from django.db import models
import comment
from student.models import Student
from products.models import Products

class Comment(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='comment')
    product = models.ForeignKey(Products,on_delete=models.CASCADE,related_name='comment')
    message = models.TextField()
    created_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} ->{self.product.name}"
    

