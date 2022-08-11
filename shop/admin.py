from django.contrib import admin

from .models import *


class ProductCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title')

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title','code', 'slug', 'price', 'discount', 'category',)
    list_display_links = ('id', 'title')

class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)

class ProductCharacteristicAdmin(admin.ModelAdmin):
    list_display = ('id', 'characteristic', 'value', 'size')
    # list_display_links = ('product',)

class ProductSliderAdmin(admin.ModelAdmin):
    list_display = ('product', 'photo')

class ProductSubCategoryAdmin(admin.ModelAdmin):
    list_display_links = ('id','title', 'category')
    list_display = ('id','title', 'category')

class RequsetMessageAdmin(admin.ModelAdmin):
    list_display_links = ('id', 'phone', 'address')
    list_display = ('id', 'phone', 'address', 'comment', 'mounting', 'paymentMethod')


admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Characteristic, CharacteristicAdmin)
admin.site.register(ProductCharacteristic, ProductCharacteristicAdmin)
admin.site.register(ProductSlider, ProductSliderAdmin)
admin.site.register(TypeCharacteristic)
admin.site.register(RequestMessage, RequsetMessageAdmin)
admin.site.register(ProductSubCategory, ProductSubCategoryAdmin)
