from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('products/<int:category_id>/', views.products, name='category'),
    path('product/<int:pk>/', views.product, name='product'),
    path('products/page/<int:page>/', views.products, name='page'),
]
