from rest_framework import serializers
from blog_app.models import Post, Like


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    # def create(self, validated_data):
    #     print(self.context['request'].user.id)
    #     instance = super(PostSerializer, self).create(validated_data)
    #     instance.user = self.context['request'].user
    #     instance.save()
    #     return instance

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'