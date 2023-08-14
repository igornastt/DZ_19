from django.urls import path
from .views import contacts, IndexView, ProductDetailView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', contacts),
    path('product/<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),
]
