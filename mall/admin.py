from django.contrib import admin
from .models import Item, Category

# Register your models here.

admin.site.register(Item)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
admin.site.register(Category, CategoryAdmin)
