from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from.serializers import productSerializer
from rest_framework import status
from.models import Products
from django.shortcuts import get_object_or_404


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
       

class PoductDetail(APIView):
   def get(self,request,pk):
      product = get_object_or_404(Products,pk=pk)
      serializer = productSerializer(product) 
      return Response(serializer.data) 
   
   def put(self,request,pk):
      product = get_object_or_404(Products,pk=pk)  
      serializer = productSerializer(product,data = request.data)  
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data) 
      return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND) 
   def delete(self,request,pk):
      product = get_object_or_404(Products,pk=pk)
      product.delete()
      return Response('delete be succefuly!')
       
      


