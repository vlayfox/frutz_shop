# Generated by Django 4.1.3 on 2022-11-28 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_tag_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='tg_art',
        ),
        migrations.AddField(
            model_name='article',
            name='tg_art',
            field=models.ManyToManyField(to='blog.tag', verbose_name='Теги'),
        ),
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(blank=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
    ]
