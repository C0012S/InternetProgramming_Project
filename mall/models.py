from django.db import models

# Create your models here.

class Item(models.Model):
    item_name = models.CharField(max_length=50) # 상품명
    item_explanation = models.TextField() # 상품 설명
#    item_image = models.ImageField(upload_to='mall/images/%Y/%m/%d/', blank=True)  # 상품 이미지
    item_price = models.IntegerField() # 가격

#    maker = models.ForeignKey(Maker, null=True, blank=True, on_delete=models.SET_NULL) # 제조사 포함 (다대일 관계)
#    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL) # 카테고리 포함 (다대일 관계)

    item_size = models.CharField(max_length=20) # 사이즈
    item_material = models.CharField(max_length=40) # 소재

    def __str__(self):
        return f'[{self.pk}]{self.item_name}'

    def get_absolute_url(self):
        return f'/mall/{self.pk}'
