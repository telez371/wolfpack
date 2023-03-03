from rest_framework.serializers import ModelSerializer
from shop.models import Product
from .category_serializer import CategorySerializer


class ProductSerializer(ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ('name',
                  'image',
                  'description',
                  'price',
                  'category',
                  )

