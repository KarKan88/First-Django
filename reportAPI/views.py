"""
Views
"""
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UILayout, Category, Attribute
from .serializers import UILayoutSerializer, CategorySerializer, AttributeSerializer
from django.core import serializers

class ListUILayoutView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = UILayout.objects.all()
    serializer_class = UILayoutSerializer

class ListCategoryView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ListAttributeView(generics.ListAPIView):
    serializer_class = AttributeSerializer    
    model = serializer_class.Meta.model
    def get_queryset(self):
        id = self.kwargs['id']
        queryset = self.model.objects.filter(category_id=id)
        return queryset
