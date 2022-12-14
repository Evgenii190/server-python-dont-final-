# Generated by Django 4.0.6 on 2022-07-22 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_remove_product_photocard_productslider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productslider',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product', to='shop.product', verbose_name='Категория продукта'),
        ),
    ]
