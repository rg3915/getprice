from django.db import models


class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        'criado em', auto_now_add=True, auto_now=False)
    modified = models.DateTimeField(
        'modificado em', auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class Category(models.Model):
    category = models.CharField('categoria', max_length=50, unique=True)

    class Meta:
        ordering = ['category']
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.category


class Product(models.Model):
    product = models.CharField('produto', max_length=50, unique=True)
    category = models.ForeignKey('Category', verbose_name='categoria')

    class Meta:
        ordering = ['category', 'product']
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'

    def __str__(self):
        return self.product


class Store(models.Model):
    store = models.CharField('loja', max_length=50)

    class Meta:
        ordering = ['store']
        verbose_name = 'loja'
        verbose_name_plural = 'lojas'

    def __str__(self):
        return self.store


class Quotation(TimeStampedModel):
    product = models.ForeignKey('Product', verbose_name='produto')
    store = models.ForeignKey('Store', verbose_name='loja')
    price = models.DecimalField(u'preço', max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField('quantidade', default=0)

    class Meta:
        ordering = ['product__product']
        verbose_name = 'cotação'
        verbose_name_plural = 'cotações'


class Exam(models.Model):
    name = models.CharField(max_length=50)
    exam = models.PositiveIntegerField()
    score = models.PositiveIntegerField()
