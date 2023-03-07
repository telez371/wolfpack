from django.urls import path
from .views import ProductCardView
from .views import ProductByCategoryListView
from .views import ProductSearchView
from .views import CatalogListView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Shop API",
        default_version='v1',
        description="Docs",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('product/<int:product_id>/', ProductCardView.as_view()),
    path('catalog/', CatalogListView.as_view()),
    path('catalogsearch/', ProductSearchView.as_view()),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('<slug:category_slug>/', ProductByCategoryListView.as_view()),
]
