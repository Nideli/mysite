from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'get_html_photo')
    list_display_links = ('id', 'name')
    search_fields = ['name']
    def get_html_photo(self,object): #обджект-ссылка на текущую запись
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50>")
    get_html_photo.short_description='Миниатюра'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    search_fields = ['name']

class CatalogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ['title']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Catalog, CatalogAdmin)