# Generated by Django 4.0.6 on 2022-07-22 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_alter_product_contentpreview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='photoCard',
        ),
        migrations.CreateModel(
            name='ProductSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фотография')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='shop.product', verbose_name='Категория продукта')),
            ],
        ),
    ]
