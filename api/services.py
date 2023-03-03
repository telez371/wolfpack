from shop.models import Product


def get_available_product_by_id_and_slug(product_id: int, slug: str) -> Product:
    return Product.objects.filter(id=product_id, available=True, slug=slug).first()


def get_available_product_list() -> list[Product]:
    return Product.objects.filter(available=True)


def get_available_product_list_by_category_slug(category_slug: str) -> list[Product]:
    return Product.objects.filter(available=True, category__slug=category_slug).select_related('category')

