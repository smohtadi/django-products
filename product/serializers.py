from rest_framework import serializers

from category.serializers import CategorySerializer
from tag.serializers import TagSerializer
from product import models


class ProductSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many = True)
    category = CategorySerializer()

    class Meta:
        model = models.Product
        fields = ["id", "code", "description", "price", "category", "tags"]