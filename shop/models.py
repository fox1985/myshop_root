from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Имя категории')
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='категория')
    name = models.CharField(max_length=200, db_index=True, verbose_name='Наименование товара')
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='poducts/%Y/%m/%d/', blank=True, verbose_name='Изображение')
    description = models.TextField(blank=True, verbose_name='описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    available = models.BooleanField(default=True, verbose_name='Опубликовано')
    created = models.DateTimeField(auto_now_add=True, verbose_name='созданный')
    updated = models.DateTimeField(auto_now=True, verbose_name='обновленный')

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'))
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])



