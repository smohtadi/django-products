from rest_framework.generics import ListAPIView
from category.models import Category
from category.serializers import CategorySerializer


class CategoryListView(ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()
