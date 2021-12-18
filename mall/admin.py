from django.contrib import admin
from .models import Item, Category, Comment, Maker

# Register your models here.

admin.site.register(Item)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
admin.site.register(Category, CategoryAdmin)

admin.site.register(Comment)

class MakerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'maker_slug':('maker_name',)}
admin.site.register(Maker, MakerAdmin)