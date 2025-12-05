from rest_framework import serializers
from student.serializers import StudentSerializer
from products.serializers import productSerializer
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    product = productSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['product', 'message']
