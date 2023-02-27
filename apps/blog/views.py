from django.urls import reverse

from apps.blog.models import BlogCategory, Article, Tag
from django.shortcuts import render


def blog_category_list(request):
    blog_categories = BlogCategory.objects.all()
    return render(request, 'blog/category_list.html', {"categories": blog_categories})


def aticle_list(request, category_id):
    articles = Article.objects.filter(category_id=category_id)
    category = BlogCategory.objects.get(id=category_id)
    breadcrumbs = {reverse('blog_category_list'): 'Блог', 'current': category.name
                   }
    return render \
        (request, 'blog/article_list.html',
         {'articles': articles, 'category': category, 'breadcrumbs': breadcrumbs})


def article_view(request, category_id, article_id):
    category = BlogCategory.objects.get(id=category_id)
    article = Article.objects.get(id=article_id)
    return render(request, 'blog/article_view.html', {"category": category, "article": article})


def found_tag_view(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    articles = Article.objects.filter(tags=tag)
    return render(request, 'blog/found_tag.html', {'tag': tag, 'articles': articles})
