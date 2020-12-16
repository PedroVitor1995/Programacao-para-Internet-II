from django.db import models

# Create your models here.

class Address(models.Model):
	street = models.CharField(max_length=300)
	suite = models.CharField(max_length=300)
	city = models.CharField(max_length=300)
	zipcode = models.CharField(max_length=300)

class Profile(models.Model):
	name = models.CharField(max_length=500)
	email = models.EmailField(max_length=500)
	address = models.OneToOneField(Address, related_name='address', on_delete=models.CASCADE)

	class Meta:
		ordering = ('name',)
		
class Post(models.Model):
	title = models.TextField()
	body = models.TextField()
	userId = models.ForeignKey(Profile, related_name='posts', on_delete=models.CASCADE)

class Comment(models.Model):
	name = models.TextField()
	email = models.EmailField(max_length=500)
	body = models.TextField()
	postId = models.ForeignKey(Post,related_name='comments', on_delete=models.CASCADE)
