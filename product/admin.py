from django.contrib import admin
from product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ["category", "tags"]
    fieldsets = (
        ("Basic Information", {"fields": ("code", "description", "price")}),
        ("Categorization", {"fields": ("category", "tags")})
    )
    list_display = ["code", "description", "price", "get_category", "get_tags"]
    list_filter = ["category__name", "tags"]
    ordering = ["description"]
    search_fields = ["description"]

    def get_category(self, product: Product) -> str:
        if product.category:
            return product.category.name
        return "-"

    def get_tags(self, product: Product) -> str:
        if product.tags.exists():
            return ", ".join([t.name for t in product.tags.all()])
        return "-"

    get_category.admin_order_field = "category__name"
    get_category.short_description = "Category"

    get_tags.admin_order_field = "tags__name"
    get_tags.short_description = "Tags"
