from rest_framework import serializers
from tag import models

class TagSerializer(serializers.ModelSerializer):
    """Serializer for the tag model"""
    class Meta:
        model = models.Tag
        fields = ["id", "name"]