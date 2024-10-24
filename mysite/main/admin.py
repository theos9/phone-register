from django.contrib import admin
from .models import mobile_phone,brand

@admin.register(mobile_phone)
class mobile_admin(admin.ModelAdmin):
    list_display=['brand','model','price','color','screen_size','status','manufacturer_country']
    list_per_page = 15
    fieldsets=(
        ('مشخصات موبایل',{'fields':('brand','model','manufacturer_country')}),
        ('قیمت',{'fields':('price',)}),
        ('اطلاعات اضافه',{'fields':('color','screen_size')}),
        ('وضعیت',{'fields':('status',)}),
    )

@admin.register(brand)
class brand_admin(admin.ModelAdmin):
    list_display=['name','nationality']
    list_per_page = 10