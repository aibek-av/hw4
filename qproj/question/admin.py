from django.contrib import admin
from qproj.question.models import Post
from qproj.question.models import Comment
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)