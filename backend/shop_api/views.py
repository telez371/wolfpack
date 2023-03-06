from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .services import get_available_product_by_id
from .services import get_available_product_list_by_category_slug

from .serializers import ProductSerializer
from .serializers import CategorySerializer

from shop.models import Category


class ProductCardView(APIView):

    @staticmethod
    def get(request, product_id: int) -> Response:
        product = get_available_product_by_id(product_id)
        if not product:
            return Response("Product doesn't exist", status=status.HTTP_404_NOT_FOUND)
        product_card = ProductSerializer(product)
        return Response(product_card.data, status=status.HTTP_200_OK)


class ProductListView(APIView):

    @staticmethod
    def get(request, category_slug: str) -> Response:
        product_list = get_available_product_list_by_category_slug(category_slug)
        if not product_list:
            return Response("Category doesn't exist", status=status.HTTP_404_NOT_FOUND)
        return Response(ProductSerializer(product_list, many=True).data, status.HTTP_200_OK)


class CatalogListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
