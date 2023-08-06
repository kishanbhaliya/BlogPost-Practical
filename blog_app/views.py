from rest_framework import generics
from blog_app.models import Post, Like
from blog_app.serializers import PostSerializer, LikeSerializer
from rest_framework.permissions import IsAuthenticated
from auth_app.permissions import UserAuthentication, AllowAnyReadOnly
# Create your views here.

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [UserAuthentication]
    permission_classes = [IsAuthenticated|AllowAnyReadOnly]

    def perform_create(self, serializer):
        # Set the authenticated user as the 'user' field in the Post model
        serializer.save(created_by=self.request.user.id)

class PostRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [UserAuthentication]
    permission_classes = [IsAuthenticated|AllowAnyReadOnly]

    def perform_update(self, serializer):
        # Set the authenticated user as the 'updated_by' field in the Post model
        serializer.save(updated_by=self.request.user.id)

class LikeListCreateView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class LikeRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
