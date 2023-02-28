from rest_framework.routers import DefaultRouter
from apps.api.blog.views import ArticleViewSerializer


urlpatterns=[]

roater=DefaultRouter()
roater.register('article',ArticleViewSerializer,basename='article')

urlpatterns+=roater.urls