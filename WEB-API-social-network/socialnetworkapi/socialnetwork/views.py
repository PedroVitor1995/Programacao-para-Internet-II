from django.shortcuts import render
from django.http import *
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import *
from .serializers import *
from socialnetworkapi import *

import os.path
import json

# Create your views here.

class ImportJson(generics.GenericAPIView):
	file = 'WEB-API-social-network\socialnetworkapi\db.json'
	if os.path.exists(file):
		data = json.load(open(file))

		if Profile.objects.count() == 0:
			for profile in data['users']:
				profile_serializer = ProfileSerializer(data=profile)
				if profile_serializer.is_valid():
					profile_serializer.save()
		
		if Post.objects.count() == 0:
			for post in data['posts']:
				post_serializer = PostSerializer(data=post)
				if post_serializer.is_valid():
					post_serializer.save()
		
		if Comment.objects.count() == 0:
			for comment in data['comments']:
				comment_serializer = CommentSerializer(data=comment)
				if comment_serializer.is_valid():
					comment_serializer.save()


# http://servidor/profiles
class ProfileList(generics.ListCreateAPIView):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer
	name = 'profile-list'

# http://servidor/profiles/id	
class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer
	name = 'profile-detail'

# http://servidor/profile-posts/
class ProfileListPostList(generics.ListAPIView):
	queryset = Profile.objects.all()
	serializer_class = ProfilePostSerializer
	name = 'profile-list-post-list'

# http://servidor/profile-posts/id/
class ProfileDetailPostList(generics.RetrieveAPIView):
	queryset = Profile.objects.all()
	serializer_class = ProfilePostSerializer
	name = 'profile-detail-post-list'

# http://servidor/posts-comments
class PostListCommentList(generics.ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostCommentSerializer
	name = 'post-list-comment-list'

# http://servidor/profile-posts/1/
class PostDetailCommentList(generics.RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class = PostCommentSerializer
	name = 'post-detail-comment-list'

# http://servidor/posts/id/comments
class PostCommentList(APIView):

	name = 'post-comment-list'

	def get_post(self, pk): 
		try:
			return Post.objects.get(pk=pk)
		except Post.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		post = self.get_post(pk)
		comment_serializer = CommentSerializer(post.comments, many=True)
		return Response(comment_serializer.data)

	def post(self, request, pk, format=None):
		comment = request.data
		comment['postId'] = self.get_post(pk).id
		comment_serializer = CommentSerializer(data=comment)
		
		if comment_serializer.is_valid():
			comment_serializer.save()
			return Response(comment_serializer.data, status=status.HTTP_201_CREATED)
		
		return Response(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# http://servidor/posts/id/comments/id
class PostCommentDetail(APIView):
	
	name = 'post-comment-detail'

	def get_post(self, pk): 
		try:
			return Post.objects.get(pk=pk)
		except Post.DoesNotExist:
			raise Http404

	def get_comment(self, post_pk, comment_pk):
		try:
			post = self.get_post(post_pk)
			return post.comments.get(pk=comment_pk)
		except Comment.DoesNotExist:
			raise Http404

	def get(self, request, post_pk, comment_pk, format=None):
		comment = self.get_comment(post_pk,comment_pk)
		comment_serializer = CommentSerializer(comment)
		return Response(comment_serializer.data)

	def put(self, request, post_pk, comment_pk, format=None):
		comment = self.get_comment(post_pk,comment_pk)
		comment_data = request.data
		comment_data['postId'] = self.get_comment(post_pk,comment_pk).postId.id
		comment_serializer = CommentSerializer(comment, data=comment_data)
		
		if comment_serializer.is_valid():
			comment_serializer.save()
			return Response(comment_serializer.data)
		
		return Response(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, post_pk, comment_pk, format=None):
		comment = self.get_comment(post_pk,comment_pk)
		comment.delete()
		return Response(status=status.HTTP_200_OK)

class ProfilePostComment(APIView):

	name = 'profile-post-comment'

	def get(self, request, format=None):
		result = []
		profiles = Profile.objects.all()
		for profile in profiles:
			profile_data = {}
			
			profile_data['id'] = profile.id
			profile_data['name'] = profile.name
			posts = profile.posts.count()
			comments = 0

			for post in profile.posts.all():
				comments += post.comments.count()

			profile_data['total_posts'] = posts
			profile_data['total_comments'] = comments

			result.append(profile_data)

		return Response(result)
		
class EndpointList(generics.GenericAPIView):

	name = 'api-root'

	def get(self, request,*args, **kwargs):	
		root_url = 'http://127.0.0.1:8000/'
		return Response({
			'profiles': reverse(ProfileList.name, request=request),
			'profiles-posts': reverse(ProfileListPostList.name, request=request),
			'posts-comments': reverse(PostListCommentList.name, request=request),
			'post-detail-comments' : root_url + 'posts/<int:pk>/comments',
			'profiles-posts-comments': reverse(ProfilePostComment.name, request=request)			
		})