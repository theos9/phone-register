from rest_framework import serializers
from .models import brand, mobile_phone

class brand_serializer(serializers.ModelSerializer):
    class Meta:
        model = brand
        fields = ['id', 'name', 'nationality']

class mobile_serializer(serializers.ModelSerializer):
    brand = brand_serializer()

    class Meta:
        model = mobile_phone
        fields = ['id', 'brand', 'model', 'price', 'color', 'screen_size', 'status', 'manufacturer_country']
