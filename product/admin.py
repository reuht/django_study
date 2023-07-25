from django.contrib import admin
from .models import Category, Product

#config el admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

class ProductAdmin(admin.ModelAdmin):
    exclude = ('create',)
    list_display = ('id', 'name', 'stock', 'puntaje')

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)


