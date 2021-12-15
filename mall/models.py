from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True) # 카테고리 이름
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True) # URL

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return f'/mall/category/{self.slug}'

    class Meta:
        verbose_name_plural = 'Categories'

class Item(models.Model):
    item_name = models.CharField(max_length=50) # 상품명
    item_explanation = models.TextField() # 상품 설명
#    item_image = models.ImageField(upload_to='mall/images/%Y/%m/%d/', blank=True)  # 상품 이미지
    item_price = models.IntegerField() # 가격

    item_size = models.CharField(max_length=20) # 사이즈
    item_material = models.CharField(max_length=40) # 소재

#    maker = models.ForeignKey(Maker, null=True, blank=True, on_delete=models.SET_NULL) # 제조사 포함 (다대일 관계)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL) # 카테고리 포함 (다대일 관계)

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'[{self.pk}]{self.item_name} :: {self.author}'

    def get_absolute_url(self):
        return f'/mall/{self.pk}'
