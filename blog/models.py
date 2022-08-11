from django.db import models

class BlogCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Url')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категории постов'
        verbose_name_plural = 'Категории постов'

class BlogPost(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Url')
    previewContent = models.CharField(max_length=255, verbose_name='Предпросматриваемый контент')
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.PROTECT, related_name='posts', verbose_name='Категория')

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = 'Список постов'
        verbose_name_plural = 'Список постов'


