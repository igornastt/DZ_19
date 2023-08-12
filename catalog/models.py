from django.db import models

NULLABLE = {'blank': True, 'null': True}  # константа для необязательного поля

class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='наименование')
    text = models.TextField(max_length=10000, verbose_name='описание')
    image = models.ImageField(verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория', **NULLABLE)
    price = models.IntegerField(verbose_name='цена', **NULLABLE)
    date_creation = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    date_change = models.DateTimeField(verbose_name='дата изменений', auto_now=True)


    def __str__(self):
        # Строковое отображение объекта
        return f'{self.title}. {self.text}'

    class Meta:
        verbose_name = 'продукт'  # Настройка для наименования одного объекта
        verbose_name_plural = 'продукты'
        ordering = ('title',)

class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='наименование')
    text = models.TextField(max_length=10000, verbose_name='описание')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.title}. {self.text}'

    class Meta:
        verbose_name = 'кетегория'  # Настройка для наименования одного объекта
        verbose_name_plural = 'категории'
        ordering = ('title',)

class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    description = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='blog/', verbose_name='изображение', **NULLABLE)
    creation_date = models.DateTimeField(verbose_name='дата создания')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return f'{self.title}, {self.description}'

    class Meta:
        verbose_name = "статья"
        verbose_name_plural = "статьи"
