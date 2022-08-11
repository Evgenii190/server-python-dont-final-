from django.contrib import admin

from .models import Characteristic, ProjectCategory, Project, ProjectCharacteristic

class ProjectsCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title')

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title', 'slug', 'price', 'category')
    list_display_links = ('id', 'title')

class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)

class ProjectCharacteristicAdmin(admin.ModelAdmin):
    list_display = ('project','characteristic',)
    list_display_links = ('project',)


admin.site.register(ProjectCategory, ProjectsCategoryAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Characteristic, CharacteristicAdmin)
admin.site.register(ProjectCharacteristic, ProjectCharacteristicAdmin)