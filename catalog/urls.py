from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import index, home, product_list, contacts, product_detail

app_name = CatalogConfig.name

urlpatterns = [
    path('', index),
    path('home/', home, name='home'),
    path('product_list/', product_list, name='product_list'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', product_detail, name='product_detail')
]
