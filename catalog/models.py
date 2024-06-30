from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(
        max_length=25,
        verbose_name="Категория товара",
        help_text="Укажите наименование категории товара",
    )
    description = models.TextField(
        verbose_name="Описание категории товара",
        help_text="Укажите описание категории товара",
        **NULLABLE
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=25,
        verbose_name="Наименование",
        help_text="Укажите наименование товара",
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Укажите описание товара",
        **NULLABLE
    )
    image = models.ImageField(
        upload_to="catalog/image",
        verbose_name="Изображение",
        help_text="Загрузите изображение товара",
        **NULLABLE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Выберите категорию товара",
        **NULLABLE,
        related_name='products',
    )
    price = models.IntegerField(verbose_name="Цена за покупку", help_text="Укажите цену товара",)

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата последнего изменения"
    )

    authorized_user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.SET_NULL, **NULLABLE)

    class Meta:
        verbose_name = " Товар"
        verbose_name_plural = "Товары"
        ordering = ("name", "category")
    class Meta:
        verbose_name = " Товар"
        verbose_name_plural = "Товары"
        ordering = ("name", "category")

    def __str__(self):
        return f'{self.name} {self.price} {self.category}'


