from rest_framework import generics , filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import brand, mobile_phone
from .Serializers import brand_serializer, mobile_serializer
from django.db.models import F

#برای لیست کردن و ساخت نوع برند ها
class brand_list_create_view(generics.ListCreateAPIView):
    queryset = brand.objects.all()
    serializer_class = brand_serializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['nationality']

    
#برای جزیات و اپدیت یک برند
class brand_retrieve_update_view(generics.RetrieveUpdateAPIView):
    queryset = brand.objects.all()
    serializer_class = brand_serializer

# برای لیست کردن و ساخت گوشی ها
class mobile_list_create_view(generics.ListCreateAPIView):
    queryset = mobile_phone.objects.all()
    serializer_class = mobile_serializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['brand__name']
    # search_fields = ['brand__name']

#برای جزیات و اپدیت یک گوشی
class mobile_retrieve_update_view(generics.RetrieveUpdateAPIView):
    queryset = mobile_phone.objects.all()
    serializer_class = mobile_serializer

# برای این کار: لیست تمامی موبایلهایی که ملیت برند با کشور سازندهی آن برابر است 
class filter_brand_country(generics.ListAPIView):
    serializer_class = mobile_serializer
    def get_queryset(self):
        return mobile_phone.objects.filter(brand__nationality=F('manufacturer_country'))
