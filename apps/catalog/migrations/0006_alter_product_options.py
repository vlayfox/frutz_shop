# Generated by Django 4.1.3 on 2023-02-18 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товары.', 'verbose_name_plural': 'Товар.'},
        ),
    ]
