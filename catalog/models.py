from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):

    title = models.CharField(max_length=200, verbose_name='Наименование')
    description = models.CharField(max_length=500, verbose_name='Описание')

    def __str__(self):
        return f'{self.title} {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('title',)


class Product(models.Model):

    title = models.CharField(max_length=200, verbose_name='Наименование')
    description = models.CharField(max_length=500, verbose_name='Описание')
    avatar = models.ImageField(upload_to='products/', verbose_name='Изображение (превью)', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='Категория',
                                 **NULLABLE, related_name='products')
    price = models.IntegerField(verbose_name='Цена за покупку')
    created_at = models.DateField(verbose_name='Дата создания (записи в БД)', **NULLABLE)
    updated_at = models.DateField(verbose_name='Дата последнего изменения (записи в БД)', **NULLABLE)

    def __str__(self):
        return f'{self.title} {self.description} {self.category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('title',)



