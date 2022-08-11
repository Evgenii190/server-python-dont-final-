from rest_framework import serializers
from .models import Product, ProductCategory, ProductCharacteristic, ProductSlider, ProductSubCategory

from rest_framework import serializers

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ('id', 'title', 'slug')

class ProductCharacteristicSerializer(serializers.ModelSerializer):
    params = serializers.CharField(source='characteristic')

    class Meta:
        model = ProductCharacteristic
        fields = [ 'value', 'params', 'type', 'size']

class ProductSerializer(serializers.ModelSerializer):
    characteristics = ProductCharacteristicSerializer(many=True)
    products = serializers.CharField(source='category')
    sub = serializers.CharField(source='subcategory')
    class Meta:
        model = Product
        fields = ['id', 'title', 'slug', 'contentPreview',
        'price', 'content' ,'discount', 'photo',
        'code', 'products','category', 'characteristics', 'subcategory', 'sub']



class ProductSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSlider
        fields = ('product', 'photo')

class ProductSubCategorySerializer(serializers.ModelSerializer):
    category_set = serializers.CharField(source='category')
    filters = ProductCharacteristicSerializer(many=True)
    class Meta:
        model = ProductSubCategory
        fields = ('title', 'category_set', 'category',  'filters', 'id')


