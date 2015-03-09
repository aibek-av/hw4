from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
	
	author = models.CharField(max_length=1000)
	title = models.CharField(max_length=1000)
	text = models.TextField()
	pub_date = models.DateTimeField(auto_now_add=timezone.now)
	upd_date = models.DateTimeField(auto_now=timezone.now)
	is_public = models.BooleanField(default=False)

class Comment(models.Model):

	author = models.CharField(max_length=1000)
	text = models.TextField()
	pub_date = models.DateTimeField(auto_now_add=timezone.now)
	post = models.ForeignKey(Post)