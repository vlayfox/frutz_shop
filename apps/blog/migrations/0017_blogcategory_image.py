# Generated by Django 4.1.3 on 2022-12-22 21:00

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_remove_blogcategory_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcategory',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='blog/category/', verbose_name='Изображение'),
        ),
    ]