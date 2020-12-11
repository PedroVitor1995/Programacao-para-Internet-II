from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=300, blank=True, default='')
    email = models.EmailField(max_length=150, blank=False, null=False)

class Post(models.Model):
    userId = models.ForeignKey(Profile, related_name='profile_post', on_delete=models.CASCADE)
    title = models.TextField()
    body = models.TextField()

class Comment(models.Model):
    postId = models.ForeignKey(Post,related_name='post_comment', on_delete=models.CASCADE)
    name = models.CharField(max_length=300, blank=True, default='')
    email = models.EmailField(max_length=150, blank=False, null=False)
    body = models.TextField()
