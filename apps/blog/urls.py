from django.urls import path
from apps.blog.views import blog_category_list, aticle_list,article_view

urlpatterns = [
    path('', blog_category_list, name='blog_category_list'),
    path('<int:category_id>/', aticle_list, name='blog_article_list'),
    path('<int:category_id>/<int:article_id>/', article_view, name='blog_article_view')
]