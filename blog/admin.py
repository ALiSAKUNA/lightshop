from django.contrib import admin
from .models import blog , blog_comment
# Register your models here.
admin.site.register(blog)
admin.site.register(blog_comment)