from django.urls import path
from apps.api.catalog.views import ProductListView, \
    ProductDeleteView, ProductDetailView, \
    ProductCreateView, CategoryViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('product/', ProductListView.as_view()),
    path('product/<int:pk>/', ProductDetailView.as_view()),
    path('product/create/', ProductCreateView.as_view()),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view()),

]
router = DefaultRouter()
router.register('category', CategoryViewSet, basename='category')
urlpatterns += router.urls
