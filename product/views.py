from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from product.models import Product
from product.serializers import ProductSerializer


class ProductPageNumberPagination(PageNumberPagination):
    page_query_param = "page"
    page_size_query_param = "page-size"
    page_size = 10
    max_page_size = 50


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = ProductPageNumberPagination

    def get_queryset(self):
        query_set = Product.objects.all()
        query_params = self.request.query_params
        sort_map = {"description": "description", "-description": "-description"}
        category_id = None
        if query_params.get("category", ""):
            try:
                category_id = int(query_params.get("category", ""))
            except:
                raise ValidationError(detail={"category": "A valid integer is required"})
        search_query = query_params.get("q", "").strip()
        sort = sort_map.get(query_params.get("sort", ""), "description")
        tag_ids = []
        if query_params.get("tags", ""):
            for tid in query_params.get("tags", "").split(","):
                try:
                    tag_ids.append(int(tid))
                except:
                    raise ValidationError(detail={"tags": "A valid integer is required"})

        query_set = query_set.select_related("category").prefetch_related("tags")
        if search_query:
            query_set = query_set.filter(description__icontains=search_query)
        if category_id:
            query_set = query_set.filter(category_id=category_id)
        if tag_ids:
            query_set = query_set.filter(tags__in=tag_ids).distinct()
        query_set = query_set.order_by(sort_map.get(sort, "created_at"))
        return query_set
