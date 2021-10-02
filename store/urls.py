from django.urls import path

from . import views

app_name = "store"

urlpatterns = [
    path("api/", views.ProductListView.as_view(), name="store_home"),
    path("api/add_product", views.ProductCreateView.as_view(), name="add_product"),
    path('api/product/<int:pk>',views.ProductUpdateAPIView.as_view(),name="update_product"),
    path('api/product-delete/<int:pk>',views.ProductDeleteAPIView.as_view(),name="delete_product"),
    path("api/category/", views.CategoryListView.as_view(), name="categories"),
    path("api/<slug:slug>/", views.Product.as_view(), name="product"),
    path("api/category/<slug:slug>/", views.CategoryItemView.as_view(), name="category_item"),
]