from django.urls import path
from .views import brand_list_create_view, brand_retrieve_update_view, mobile_list_create_view, mobile_retrieve_update_view, filter_brand_country

urlpatterns = [
    path('brands/', brand_list_create_view.as_view()),
    path('brands/<int:pk>/', brand_retrieve_update_view.as_view()),
    path('mobiles/', mobile_list_create_view.as_view()),
    path('mobiles/<int:pk>/', mobile_retrieve_update_view.as_view()),
    path('mobiles/brand_country/', filter_brand_country.as_view()),
]
