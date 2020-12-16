from django.shortcuts import render
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

# http://servidor/posts/id/comments/id


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
		return Response({
			'profiles': reverse(ProfileList.name, request=request),
			'profiles-posts': reverse(ProfileListPostList.name, request=request),
			'posts-comments': reverse(PostListCommentList.name, request=request),
			'profiles-posts-comments': reverse(ProfilePostComment.name, request=request)
			})