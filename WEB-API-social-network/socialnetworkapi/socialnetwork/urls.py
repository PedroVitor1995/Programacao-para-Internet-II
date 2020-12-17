from django.urls import path
from .views import *

urlpatterns = [
	path('profiles/', ProfileList.as_view(),name=ProfileList.name),
	path('profiles/<int:pk>/', ProfileDetail.as_view(),name=ProfileDetail.name),
	path('profile-posts/', ProfileListPostList.as_view(), name=ProfileListPostList.name),
	path('profile-posts/<int:pk>', ProfileDetailPostList.as_view(), name=ProfileDetailPostList.name),
	path('posts-comments/', PostListCommentList.as_view(), name=PostListCommentList.name),
	path('posts-comments/<int:pk>', PostDetailCommentList.as_view(), name=PostDetailCommentList.name),
	path('posts/<int:pk>/comments/', PostCommentList.as_view(), name=PostCommentList.name),
	path('posts/<int:post_pk>/comments/<int:comment_pk>/', PostCommentDetail.as_view(), name=PostCommentDetail.name),
	path('profile-posts-comments/', ProfilePostComment.as_view(), name=ProfilePostComment.name),
	path('', EndpointList.as_view())
]

