from django.urls import path
from .views import ProductCardView
from .views import ProductListView

urlpatterns = [
    path('product/<int:product_id>/<slug:slug>/', ProductCardView.as_view()),
    path('product/<slug:category_slug>/', ProductListView.as_view()),
    path('product/', ProductListView.as_view()),
]
