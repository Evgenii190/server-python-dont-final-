from django.db import models

class ProductCategory(models.Model):
    title = models.CharField(max_length=64, verbose_name='Название')
    slug = models.SlugField(max_length=64, unique=True, verbose_name='Url')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория продукта'
        verbose_name_plural = 'Категории продуктов'

class ProductSubCategory(models.Model):
    title = models.CharField(max_length=64, verbose_name='Название')
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT, related_name='category', verbose_name='Категория') 
    filters = models.ManyToManyField('ProductCharacteristic', null=True, related_name='filters', verbose_name='Фильтры')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Подкатегория продукта'
        verbose_name_plural = 'Подкатегории продуктов'

class ProductSlider(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, verbose_name='Фотография')
    product =  models.ForeignKey('Product', on_delete=models.PROTECT, related_name='product', verbose_name='Продукт')

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдеры'

class Product(models.Model):
    title = models.CharField(max_length=64, verbose_name='Название продукта')
    slug = models.SlugField(max_length=64, unique=True, verbose_name='Url')
    contentPreview = models.CharField(max_length=128, verbose_name='Предпросматриваемый контент')
    price = models.CharField(max_length=20, verbose_name="Цена")
    discount = models.CharField(max_length=20, blank=True, verbose_name="Скидка")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фотография в каталоге')
    code = models.CharField(max_length=64, verbose_name="Код товара", unique=True, null=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT, related_name='products', verbose_name='Категория продукта')
    subcategory = models.ForeignKey(ProductSubCategory, null=True, on_delete=models.PROTECT, related_name='sub', verbose_name='Подкатегория продукта')
    characteristics = models.ManyToManyField('ProductCharacteristic', null=True, related_name='params', verbose_name='Характеристики продукта')
    content = models.TextField(verbose_name="Описание продукта", null=True)

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Characteristic(models.Model):
    name = models.CharField(max_length=64, verbose_name="Название")
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'
        
class TypeCharacteristic(models.Model):
    type = models.CharField(max_length=64, verbose_name="Тип")

    def __str__(self):
        return self.type

class ProductCharacteristic(models.Model):
    characteristic = models.ForeignKey(Characteristic, related_name="params", on_delete=models.PROTECT, verbose_name="Характеристика",)
    value = models.CharField(max_length=64, verbose_name="Значение")
    type = models.ForeignKey(TypeCharacteristic, related_name="types", null=True, on_delete=models.PROTECT, verbose_name="Тип",)
    size = models.CharField(max_length=64, null=True, verbose_name="Величина (мм, см и.т.п)")

    def __str__(self):
        if not self.size:
            return self.characteristic.name + ': ' + self.value
        return self.characteristic.name + ': ' + self.value + ' ' + self.size
        
    class Meta:
        verbose_name = 'Характеристика продукта'
        verbose_name_plural = 'Характеристики продуктов'

class RequestMessage(models.Model):
    phone = models.CharField(max_length=12, verbose_name="Телефон",)
    address = models.CharField(max_length=64, verbose_name="Адрес")
    comment = models.TextField(verbose_name="Комментарий к заказу",)
    mounting = models.BooleanField(verbose_name="Нужен ли монтаж")
    paymentMethod = models.CharField(max_length=64, verbose_name="Способ оплаты")
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Дата создания заявки")

    def __str__(self):
        return 'Заявка'
        
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

