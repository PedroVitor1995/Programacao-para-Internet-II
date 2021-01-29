from django.urls import path
from .views import *

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('authentication/', obtain_jwt_token),
    path('manufacturer/', ManufacturerList.as_view(), name=ManufacturerList.name),
    path('manufacturer/<int:pk>', ManufacturerCreate.as_view(), name=ManufacturerCreate.name),
    path('product/', ProductList.as_view(), name=ProductList.name),
    path('product/<int:pk>', ProductDetail.as_view(), name=ProductDetail.name),
    path('priceType/', PriceTypeList.as_view(), name=PriceTypeList.name),
    path('priceType/<int:pk>', PriceTypeDetail.as_view(), name=PriceTypeDetail.name),
    path('price/', PriceList.as_view(), name=PriceList.name),
    path('price/<int:pk>', PriceCreate.as_view(), name=PriceCreate.name),
]
