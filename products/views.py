from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from rest_framework import generics

from products.models import Product
from products.serializators import ProductSerializer

class ProductList(APIView):

    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProductDetail(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404
        
    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)