from rest_framework import serializers

from apps.blog.models import BlogCategory, Article


class BlogCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model=BlogCategory
        fields=('name'
                'image')

class ArticleReadSerializer(serializers.ModelSerializer):
    category=BlogCategorySerializers()
    class Meta:
        model=Article
        fields = ('id'
                  'category'
                  'title'
                  'user'
                  'text_preview'
                  'image'
                  'publish_date'
                  )




class ArticleWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields=('id'
                'category'
                'title'
                'user'
                'text_preview'
                'image'
                'publish_date'
                )
