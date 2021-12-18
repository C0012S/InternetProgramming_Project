from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdown

# Create your models here.

class Maker(models.Model):
    maker_name = models.CharField(max_length=50, unique=True)  # 제조사 명
    maker_address = models.CharField(max_length=100)  # 제조사 주소
    maker_number = models.CharField(max_length=20)  # 제조사 연락처

    maker_email = models.CharField(max_length=50)  # 제조사 이메일
    maker_slug = models.SlugField(max_length=100, unique=True, allow_unicode=True) # URL

    def __str__(self):
        return self.maker_name

    def get_absolute_url(self):
        return f'/mall/maker/{self.maker_slug}'

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
    item_explanation = MarkdownxField() # 상품 설명
    item_image = models.ImageField(upload_to='mall/images/%Y/%m/%d/', blank=True)  # 상품 이미지
    item_price = models.IntegerField() # 가격

    item_size = models.CharField(max_length=20) # 사이즈
    item_material = models.CharField(max_length=40) # 소재

    maker = models.ForeignKey(Maker, null=True, blank=True, on_delete=models.CASCADE) # 제조사 포함 (다대일 관계)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL) # 카테고리 포함 (다대일 관계)

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'[{self.pk}]{self.item_name} :: {self.author}'

    def get_absolute_url(self):
        return f'/mall/{self.pk}/'

    def get_content_markdown(self):
        return markdown(self.item_explanation)

class Comment(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author}::{self.content}'

    def get_absolute_url(self):
        return f'{self.item.get_absolute_url()}#comment-{self.pk}'

    def get_avatar_url(self):
        if self.author.socialaccount_set.exists():
            return self.author.socialaccount_set.first().get_avatar_url()
        else:
            return 'https://doitdjango.com/avatar/id/388/996dbf01e24f0e3b/svg/{self.author.email}/'
