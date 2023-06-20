from django.urls import path
from . import views



urlpatterns = [
    # product urls

    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('products/update/<int:pk>', views.ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product_delete'),

    #supplier_urls
    path('suppliers/', views.SupplierListView.as_view(), name='supplier_list'),
    path('suppliers/create/', views.SupplierCreateView.as_view(), name='supplier_create'),
    path('suppliers/<int:pk>', views.SupplierDetailView.as_view(), name='supplier_detail'),
    path('suppliers/update/<int:pk>', views.SupplierUpdateView.as_view(), name='supplier_update'),
    path('suppliers/delete/<int:pk>', views.SupplierDeleteView.as_view(), name='supplier_delete'),
    #category_urls

    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('categories/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('categories/update/<int:pk>', views.CategoryUpdateView.as_view(), name="category_update"),
    path('categories/delete/<int:pk>', views.CategoryDeleteView.as_view(), name="category_delete"),

    #Transaction_urls
    path('transactions/', views.TransactionListView.as_view(), name='transaction_list'),
    path('transactions/create/', views.TransactionCreateView.as_view(), name='transaction_create'),
    path('transactions/<int:pk>', views.TransactionDetailView.as_view(), name='transaction_detail'),
    path('transactions/update/<int:pk>', views.TransactionUpdateView.as_view(), name='transaction_update'),
    path('transactions/delete/<int:pk>', views.TransactionDeleteView.as_view(), name='transaction_delete'),


]