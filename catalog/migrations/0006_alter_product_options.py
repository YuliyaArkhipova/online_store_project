# Generated by Django 4.2.2 on 2024-07-03 18:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('catalog', '0005_product_is_published'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name', 'category'),
                     'permissions': [('cancellation_of_publication', 'Canceling the publication of the product')],
                     'verbose_name': ' Товар', 'verbose_name_plural': 'Товары'},
        ),
    ]
