from rest_framework import serializers
from .models import *

class ManufacturerSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Manufacturer
		fields = ['code', 'name']

class ProductSerializer(serializers.HyperlinkedModelSerializer):
	manufacturer = ManufacturerSerializer()
	class Meta:
		model = Product
		fields = ['code','description', 'manufacturer', 'quantity']

class PricetypeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = PriceType
		fields = ['description']

class PriceSerializer(serializers.HyperlinkedModelSerializer):
	product = ProductSerializer()
	priceType = PricetypeSerializer
	class Meta:
		model = Price
		fields = ['product', 'priceType', 'value']