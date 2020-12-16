from rest_framework import serializers
from .models import *

class AddressSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Address
		fields = ['street','suite','city','zipcode']
	
class ProfileSerializer(serializers.HyperlinkedModelSerializer):
	address = AddressSerializer()
	class Meta:
		model = Profile
		fields = ['url','name', 'email', 'address']

	def create(self, validated_data):
		address_data = validated_data.pop('address')
		address = Address.objects.create(**address_data)
		return Profile.objects.create(address=address ,**validated_data)

	def update(self, instance, validated_data):
		address_data = validated_data.pop('address')
		address = instance.address
		address.street = address_data.get('street', address.street)
		address.suite = address_data.get('suite', address.suite)
		address.city = address_data.get('city', address.city)
		address.zipcode = address_data.get('zipcode', address.zipcode)
		address.save()
		instance.email = validated_data.get('email', instance.email)
		instance.name = validated_data.get('name', instance.name)
		instance.save()
		return instance

class PostSerializer(serializers.HyperlinkedModelSerializer):
	userId = serializers.SlugRelatedField(queryset=Profile.objects.all(),slug_field='id')
	class Meta:
		model = Post
		fields = ['title', 'body', 'userId']

class CommentSerializer(serializers.HyperlinkedModelSerializer):
	postId = serializers.SlugRelatedField(queryset=Post.objects.all(),slug_field='id')
	class Meta:
		model = Comment
		fields = ['name', 'email', 'body', 'postId']

class PostProfileSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Post
		fields = ['title','body']

class ProfilePostSerializer(serializers.HyperlinkedModelSerializer):
	posts = PostProfileSerializer(many=True, read_only=True)
	class Meta:
		model = Profile
		fields = ['url', 'name', 'email', 'posts']

class CommentPostSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Comment
		fields = ['name', 'body' , 'email']

class PostCommentSerializer(serializers.HyperlinkedModelSerializer):
	comments = CommentPostSerializer(many=True, read_only=True)
	class Meta:
		model = Post
		fields = ['url', 'title', 'body','comments']

