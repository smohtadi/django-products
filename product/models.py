from django.db import models

from category.models import Category
from tag.models import Tag


class Product(models.Model):
    # Fields
    code = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Relationships
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="products")
    tags = models.ManyToManyField(Tag, blank=True, related_name="products")

    def __str__(self):
        return f"{self.code}"
