from django.contrib import admin
from blog_app import models

# Register your models here.
@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'created_by', 'created_at',)


@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'post', 'created_at',)


