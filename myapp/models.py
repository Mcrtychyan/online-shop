from django.db import models
from django.forms import forms


class Category(models.Model):
    name = models.CharField(max_length=200,verbose_name='Название категории',help_text='Максимум 200 символов')

    slug = models.SlugField(max_length=200,unique=True,verbose_name='URL-адрес',help_text='URL-friendly название (латинские буквы, цифры, дефисы)')

    description = models.TextField(blank=True,null=True,verbose_name='Описание',help_text='Необязательное описание категории')

    is_active = models.BooleanField(default=True,verbose_name='Активна',help_text='Отображается ли категория на сайте')

    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Дата создания')

    updated_at = models.DateTimeField(auto_now=True,)

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

        def __str__(self):
            return self.name

class Products(models.Model):
    name = models.CharField(max_length=200,verbose_name='Название товара',help_text='Максимум 200 символов')

    category_id = models.ForeignKey(
        'Category',
    on_delete=models.PROTECT,
    related_name='products',
    verbose_name='Категория товара'
    )

    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name='URL-friendly название',
        help_text='Уникальное название для URL'
    )

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Полное описание товара'
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена товара'
    )

    stock = models.IntegerField(
        default=0,
        verbose_name='Количество на складе'
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name='Доступен для продажи'
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, )

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"

    def __str__(self):
        return self.name