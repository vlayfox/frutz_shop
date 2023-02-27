# Generated by Django 4.1.3 on 2023-02-27 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_article_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='meta_description',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta Description'),
        ),
        migrations.AddField(
            model_name='article',
            name='meta_keywords',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta Keywords'),
        ),
        migrations.AddField(
            model_name='article',
            name='meta_tittle',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta Tittle'),
        ),
        migrations.AddField(
            model_name='blogcategory',
            name='meta_description',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta Description'),
        ),
        migrations.AddField(
            model_name='blogcategory',
            name='meta_keywords',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta Keywords'),
        ),
        migrations.AddField(
            model_name='blogcategory',
            name='meta_tittle',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta Tittle'),
        ),
    ]
