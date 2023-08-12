from django.urls import path
from catalog.views import contacts, IndexView, ProductDetailView, blog_list_view, BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDelete


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', contacts),
    path('product/<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),
    path('list/', blog_list_view, name='catalog_list'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('', BlogListView.as_view(), name='list'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', BlogDelete.as_view(), name='delete'),
]
