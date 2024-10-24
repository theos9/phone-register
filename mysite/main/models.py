from django.db import models

class brand(models.Model):
    name = models.CharField(max_length=100, unique=True,verbose_name='نام برند')
    nationality = models.CharField(max_length=100,verbose_name='ملیت برند')

    def __str__(self):
        return f'{self.name} {self.nationality}'
    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برند ها'

class mobile_phone(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('not_available', 'Not Available'),
    ]
    
    brand = models.ForeignKey(brand, on_delete=models.CASCADE,verbose_name='برند')
    model = models.CharField(max_length=100, unique=True,verbose_name='مدل گوشی')
    price = models.PositiveIntegerField(verbose_name='قیمت')
    color = models.CharField(max_length=50,verbose_name='رنگ')
    screen_size = models.DecimalField(max_digits=4, decimal_places=1,verbose_name='سایز صفحه نمایش')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,verbose_name='وضعیت')
    manufacturer_country = models.CharField(max_length=100,verbose_name='کشور سازنده')

    def __str__(self):
        return f"{self.brand.name} {self.model}"
    class Meta:
        verbose_name = 'موبایل'
        verbose_name_plural = 'موبایل ها'