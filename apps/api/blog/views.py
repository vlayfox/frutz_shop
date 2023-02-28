from rest_framework import viewsets, permissions
from apps.api.blog.serializers import ArticleReadSerializer, ArticleWriteSerializers
from apps.blog.models import Article


class ArticleViewSerializer(viewsets.ModelViewSet):
    serializer_class = ArticleReadSerializer
    queryset = Article.objects.all()
    def get_serializer_class(self):
        if self.action in ['create', ['update']]:
            return ArticleWriteSerializers
        return self.serializer_class

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [permission() for permission in [permissions.IsAdminUser]]
        return [permission() for permission in [permissions.AllowAny]]

