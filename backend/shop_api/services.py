from shop.models import Product


def get_available_product_by_id(product_id) -> Product:
    return Product.objects.filter(id=product_id, available=True).first()


def get_available_product_list_by_category_slug(category_slug: str) -> list[Product]:
    return Product.objects.filter(available=True, category__slug=category_slug).select_related('category')

