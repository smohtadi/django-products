from product.views import ProductListView
from django.urls import path

PRODUCT_LIST_PATH = "product_list"

urlpatterns = [
    path("products", ProductListView.as_view(), name=PRODUCT_LIST_PATH)
]