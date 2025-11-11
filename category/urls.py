from django.urls import path
from category.views import CategoryListView

urlpatterns = [
   path("categories", CategoryListView.as_view(), name="category_list") 
]