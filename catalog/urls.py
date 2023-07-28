from django.urls import path

from catalog.views import index, contact

urlpatterns = [
    path('', index)
]

urlpatterns = [
    path('', contact)
]
