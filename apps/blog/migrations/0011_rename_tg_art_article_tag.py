# Generated by Django 4.1.3 on 2022-11-28 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_tag_tg_art_article_tg_art_alter_article_text_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='tg_art',
            new_name='tag',
        ),
    ]