from rest_framework.views import APIView
from rest_framework.response import Response
from.serializers import StudentSerializer
from rest_framework import status
from.models import Student
from django.shortcuts import get_object_or_404


from django.shortcuts import render

class UsersApi(APIView):
    def get(self,request):
        students = Student.objects.all()
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
       
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SingleUserApi(APIView):
    def get(self,request,pk):
        student = get_object_or_404(Student,pk=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    def put(self,request,pk):
        student = get_object_or_404(Student,pk=pk)
        serializer = StudentSerializer(student,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    def delete(self,request,pk):
        student = get_object_or_404(Student,pK=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class LoginApi(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({"error": "Email and password required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            student = Student.objects.get(email=email)
        except Student.DoesNotExist:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        if not student.check_password(password):
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({"message": f"Welcome {student.name}"})

    


