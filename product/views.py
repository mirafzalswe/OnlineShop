from django.shortcuts import render
from rest_framework import generics
from .serializer import ProductSerializer,  ProductTypeSerializer
from .models import Product, ProductType



class ProducTypeList(generics.ListCreateAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

class ProductTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer