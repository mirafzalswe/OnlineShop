from django.shortcuts import render
from rest_framework import generics
from .serializer import ProductSerializer,  ProductTypeSerializer
from .models import Product, ProductType
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

# Paginationni  ozimzga qulay xolga keltirip oldik
class ProductAPIListPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 12

class ProducTypeList(generics.ListCreateAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = ProductAPIListPagination

class ProductTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    permission_classes = (IsAuthenticated,)


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)


def home(reqeust):
    return render(reqeust, 'product/home.html')
