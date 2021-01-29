from django.shortcuts import render
from django.http import *
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import *
from .serializers import *
from catalogoapi import *

# Create your views here.

class ManufacturerList(generics.ListCreateAPIView):
	queryset = Manufacturer.objects.all()
	serializer_class = ManufacturerSerializer
	name = 'manufacturer'

class ManufacturerCreate(generics.RetrieveUpdateDestroyAPIView):
	queryset = Manufacturer.objects.all()
	serializer_class = ManufacturerSerializer
	name = 'manufacturer-detail'

class ProductList(generics.ListCreateAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	name = 'product'

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	name = 'product-detail'

class PriceTypeList(generics.ListCreateAPIView):
	queryset = PriceType.objects.all()
	serializer_class = PricetypeSerializer
	name = 'priceType'

class PriceTypeDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = PriceType.objects.all()
	serializer_class = PricetypeSerializer
	name = 'priceType-detail'

class PriceList(generics.ListCreateAPIView):
	queryset = Price.objects.all()
	serializer_class = PriceSerializer
	name = 'price'

class PriceCreate(generics.RetrieveUpdateDestroyAPIView):
	queryset = Price.objects.all()
	serializer_class = PriceSerializer
	name = 'price-detail'
