from django.shortcuts import render
from rest_framework import generics
from .serializer import ProductSerializer,  ProductTypeSerializer
from .models import Product, ProductType
from rest_framework.permissions import IsAuthenticated

class ProducTypeList(generics.ListCreateAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    permission_classes = (IsAuthenticated,)

class ProductTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    permission_classes = (IsAuthenticated,)
    permission_classes = (IsAuthenticated,)

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)



