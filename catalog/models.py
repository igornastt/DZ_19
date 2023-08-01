from django.db import models


NULLABLE = {'blank': True, 'null':True}
class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название')
    description = models.CharField(max_length=500, verbose_name='Описание')
    image = models.ImageField(upload_to='product/', **NULLABLE, verbose_name='Изображение (превью)')
    category = models.CharField(max_length=100, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за покупку')
    date = models.DateField(verbose_name='Дата создания')
    last_modified_date = models.DateField(verbose_name='Дата последнего изменения')
    created_at = models.CharField(max_length=250, **NULLABLE, verbose_name='Создание')

    def __str__(self):
        return f'{self.name} ({self.category}): {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название')
    description = models.CharField(max_length=500, verbose_name='Описание')

    def __str__(self):
        return f'{self.name} ({self.description})'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
