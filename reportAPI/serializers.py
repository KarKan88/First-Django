"""
Song Serializer
"""
from rest_framework import serializers
from .models import UILayout, Category, Attribute, Association


class UILayoutSerializer(serializers.ModelSerializer):
    """
    Song Serializer
    """
    class Meta:
        model = UILayout
        fields = ("__all__")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("__all__")

class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ("__all__")
