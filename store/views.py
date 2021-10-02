from django.shortcuts import render
from rest_framework import generics

from . import models
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer,ProductAddSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductAddSerializer
    
class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    


class Product(generics.RetrieveAPIView):
    lookup_field = "slug"
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryItemView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return models.Product.objects.filter(
            category__in=Category.objects.get(slug=self.kwargs["slug"]).get_descendants(include_self=True)
        )


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.filter(level=1)
    serializer_class = CategorySerializer