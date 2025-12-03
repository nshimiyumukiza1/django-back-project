from rest_framework import serializers

from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        student = Student(
            name=validated_data['name'],
            email=validated_data['email']
        )
        student.set_password(validated_data['password'])
        return student

  