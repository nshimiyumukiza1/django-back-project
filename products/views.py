from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from.serializers import productSerializer
from rest_framework import status
from.models import Products

class productsData(APIView):
    def get(self,request):
        product = Products.objects.all()
        serializer = productSerializer(product,many=True) 
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self,request):
       serializer = productSerializer(data = request.data)
       if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)


