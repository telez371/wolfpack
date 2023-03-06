from django.urls import path
from .views import ProductCardView
from .views import ProductListView
from .views import CatalogListView

urlpatterns = [
    path('product/<int:product_id>/', ProductCardView.as_view()),
    path('catalog/', CatalogListView.as_view()),
    path('<slug:category_slug>/', ProductListView.as_view()),
]
