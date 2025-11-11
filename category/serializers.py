from rest_framework import serializers
from category import models

class CategorySerializer(serializers.ModelSerializer):
    """Serializer for the category model"""
    class Meta:
        model = models.Category
        fields = ["id", "name"]