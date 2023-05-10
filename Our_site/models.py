from django.db import models
from django.urls import reverse

class Catalog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def get_absolute_url(self):
        return reverse('catalog', kwargs={'catalog_slug': self.slug})
    class Meta:
        verbose_name = 'Каталог товаров'
        verbose_name_plural = 'Каталог товаров'

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название продукта')
    slug = models.SlugField(max_length=155, unique=True, db_index=True, verbose_name="URL")
    description = models.TextField(max_length=300, verbose_name='Описание продукта')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена продукта')
    image=models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Изображение товара')
    weight = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Вес продукта')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория продукта')
    expiration_date = models.DecimalField(max_digits=3, decimal_places=0, verbose_name='Срок годности')
    composition = models.TextField(verbose_name='Состав')
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'product_id': self.pk})
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['id']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    catalog = models.ForeignKey('Catalog', on_delete=models.CASCADE, verbose_name= 'Каталог категории')
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

