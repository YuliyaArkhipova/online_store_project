# Generated by Django 4.2.2 on 2024-07-01 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, help_text='Укажите страну', max_length=50, null=True, verbose_name='Страна'),
        ),
    ]
