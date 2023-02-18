from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import ResizeToFill
from django.utils.safestring import mark_safe

from apps.user.models import User
from config.settings import MEDIA_ROOT


class BlogCategory(models.Model):
    name = models.CharField(verbose_name='имя категории', max_length=255)
    image = ProcessedImageField(
        verbose_name='Изображение',
        upload_to='blog/category/',
        processors=[ResizeToFill(600, 400)],
        null=True,
        blank=True,

    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория блога'
        verbose_name_plural = 'категории блога'

    def image_tag_thumbnail(self):
        if self.image:
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image}'width='70'>")

    image_tag_thumbnail.short_description = 'Изображение'

    def image_tag(self):
        if self.image:
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image}'>")

    image_tag.short_description = 'Изображение'


class Tag(models.Model):
    name = models.CharField('Название тега', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'


class Article(models.Model):
    category = models.ForeignKey(to=BlogCategory, verbose_name='категория', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Автор', on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    text_preview = models.TextField(verbose_name='Текст-ревью', null=True, blank=True)
    text = models.TextField(verbose_name='Текст', blank=True)
    publish_date = models.DateTimeField(verbose_name='Дата публикации')
    updated_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    tags = models.ManyToManyField(to=Tag, verbose_name='Теги', blank=True)
    image = ProcessedImageField(
        verbose_name='Изображение',
        upload_to='user/',
        null=True,
        blank=True,

    )
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(200, 200)]

    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
