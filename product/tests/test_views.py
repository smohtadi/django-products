from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from category.models import Category
from product.models import Product
from product.serializers import ProductSerializer
from product.urls import PRODUCT_LIST_PATH
from tag.models import Tag


class ProductTestView(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.tagA = Tag.objects.create(name="In Demand")
        self.tagB = Tag.objects.create(name="High Price")
        self.tagC = Tag.objects.create(name="Top Rated")

        self.categoryA = Category.objects.create(name="Computer")
        self.categoryB = Category.objects.create(name="Accessory")

        self.productA = Product.objects.create(code="PP101", description="Television", price=799.99)
        self.productB = Product.objects.create(code="PP102", description="Macbook Pro", price=3569.12,
                                               category=self.categoryA)

        self.productC = Product.objects.create(code="PP103", description="Macbook Air", price=1763.00,
                                               category=self.categoryA)
        self.productD = Product.objects.create(code="PP104", description="Airpods", price=234,
                                               category=self.categoryB)
        self.productB.tags.add(self.tagA, self.tagB)
        self.productC.tags.add(self.tagB)
        self.productD.tags.add(self.tagC)
        self.productB.save()
        self.productC.save()
        self.productD.save()

    def test_get_all_products(self):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        response = self.client.get(reverse(PRODUCT_LIST_PATH))
        self.assertEqual(len(response.data['results']), len(serializer.data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_products_invalid_tag(self):
        response = self.client.get(reverse(PRODUCT_LIST_PATH, query={"tags":"abc"}))
        self.assertTrue("tags" in response.data["errors"])
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_all_products_invalid_category(self):
        response = self.client.get(reverse(PRODUCT_LIST_PATH, query={"category":"1F"}))
        self.assertTrue("category" in response.data["errors"])
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_all_products_valid_tag_invalid_category(self):
        response = self.client.get(reverse(PRODUCT_LIST_PATH, query={"tags":"1,2","category":"1.2"}))
        self.assertTrue("category" in response.data["errors"])
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_all_products_valid_category_invalid_tag(self):
        response = self.client.get(reverse(PRODUCT_LIST_PATH, query={"tags":"1*2","category":"1"}))
        self.assertTrue("tags" in response.data["errors"])
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)