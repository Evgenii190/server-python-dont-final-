from django.db import models

class ProjectCategory(models.Model):
    title = models.CharField(max_length=64, verbose_name='Название')
    slug = models.SlugField(max_length=64, unique=True, verbose_name='Url')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категории проектов'
        verbose_name_plural = 'Категории проектов'

class Project(models.Model):
    title = models.CharField(max_length=64, verbose_name='Название проекта')
    slug = models.SlugField(max_length=64, unique=True, verbose_name='Url')
    previewContent = models.CharField(max_length=120, verbose_name='Предпросматриваемый контент')
    content = models.TextField(blank=True)
    price = models.CharField(max_length=20, verbose_name="Цена")
    previewPhoto = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Предпросматриваемое фото')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фотография')
    modelPhoto = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name="Чертеж")
    category = models.ForeignKey(ProjectCategory, on_delete=models.PROTECT, related_name='projects', verbose_name='Категория проекта')

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = 'Проекты'
        verbose_name_plural = 'Проекты'



class Characteristic(models.Model):
    name = models.CharField(max_length=64, verbose_name="Название")
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'

class ProjectCharacteristic(models.Model):
    project = models.ForeignKey(Project, on_delete=models.PROTECT, verbose_name="Проект")
    characteristic = models.ForeignKey(Characteristic, related_name="params", on_delete=models.PROTECT, verbose_name="Характеристика",)
    option = models.CharField(max_length=64, verbose_name="Значение")

    def __str__(self):
        return self.option
        
    class Meta:
        verbose_name = 'Характеристика проекта'
        verbose_name_plural = 'Характеристики проектов'

