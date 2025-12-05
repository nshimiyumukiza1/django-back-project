from rest_framework import generics
from django.shortcuts import get_object_or_404
from .models import Comment
from .serializers import CommentSerializer, CommentCreateSerializer
from student.models import Student
from products.models import Products

class CommentView(generics.ListCreateAPIView):
    def get_queryset(self):
        product_id = self.kwargs.get('product_id')
        if product_id:
            return Comment.objects.filter(product_id=product_id)
        return Comment.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CommentCreateSerializer
        return CommentSerializer

    def perform_create(self, serializer):
        student_id = self.kwargs.get('student_id')
        student = get_object_or_404(Student, id=student_id) 

        product = serializer.validated_data.get('product')
        if product:
            product = get_object_or_404(product, id=product.id)

        serializer.save(student=student, product=product) 
