# Generated by Django 4.1.3 on 2023-02-18 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
    ]
