from django.contrib import admin
from .models import Post, Category, Comment

# Models

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)