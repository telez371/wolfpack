from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .services import get_available_product_by_id_and_slug
from .services import get_available_product_list
from .services import get_available_product_list_by_category_slug

from .serializers import ProductSerializer


class ProductCardView(APIView):

    @staticmethod
    def get(request, product_id: int, slug: str) -> Response:
        product = get_available_product_by_id_and_slug(product_id, slug)
        if not product:
            return Response("Product doesn't exist", status=status.HTTP_404_NOT_FOUND)
        product_card = ProductSerializer(product)
        return Response(product_card.data, status=status.HTTP_200_OK)


class ProductListView(APIView):

    @staticmethod
    def get(request, category_slug: str = None) -> Response:
        if not category_slug:
            product_list = get_available_product_list()
        else:
            product_list = get_available_product_list_by_category_slug(category_slug)
        if not product_list:
            return Response("There's no products here", status=status.HTTP_404_NOT_FOUND)
        return Response(ProductSerializer(product_list, many=True).data, status.HTTP_200_OK)
