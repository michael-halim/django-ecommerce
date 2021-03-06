from django.contrib import admin
from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('', views.index),
    path('products/', views.ProductListView.as_view(),name='products'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('products/add/', views.CreateProductView.as_view(), name='add_product'),
    path('products/update/<int:pk>/', views.UpdateProductView.as_view(), name='update_product'),
    path('products/delete/<int:pk>/', views.DeleteProductView.as_view(), name='delete_product'),
    path('products/mylistings/', views.my_listings, name='my_listings'),

]   
