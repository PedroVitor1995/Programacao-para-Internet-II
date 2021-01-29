from django.db import models

# Create your models here.

class Manufacturer(models.Model):
	code = models.CharField(max_length=50, blank=True, default='')
	name = models.CharField(max_length=100, blank=True, default='')

	class Meta:
			ordering = ('name',)

class Product(models.Model):
	code = models.CharField(max_length=75, blank=True, default='')
	description = models.CharField(max_length=200, blank=True, default='')
	quantity = models.DecimalField(max_digits = 15 ,decimal_places=2)
	manufacturer = models.ForeignKey(Manufacturer, related_name='manufacturers', on_delete=models.CASCADE)

	class Meta:
		ordering = ('description',)

class PriceType(models.Model):
	description = models.CharField(max_length=50, blank=True, default='')

class Price(models.Model):
	product = models.ForeignKey(Product, related_name='products', on_delete=models.CASCADE)
	priceType = models.ForeignKey(PriceType, related_name='priceTypes', on_delete=models.CASCADE)
	value = models.DecimalField(max_digits = 10, decimal_places=4)
