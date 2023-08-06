from rest_framework import generics, permissions
from blog_app.models import Post, Like
from blog_app.serializers import PostSerializer, LikeSerializer
from rest_framework.permissions import IsAuthenticated
from auth_app.permissions import UserAuthentication, AllowAnyReadOnly
from .permissions import IsOwnerOrReadOnly, CanViewPost
from django.db.models import Count
# Create your views here.

# class PostListCreateView(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     authentication_classes = [UserAuthentication]
#     permission_classes = [IsAuthenticated|AllowAnyReadOnly]

#     def perform_create(self, serializer):
#         # Set the authenticated user as the 'user' field in the Post model
#         serializer.save(created_by=self.request.user.id)

# class PostRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     authentication_classes = [UserAuthentication]
#     permission_classes = [IsAuthenticated|AllowAnyReadOnly]

#     def perform_update(self, serializer):
#         # Set the authenticated user as the 'updated_by' field in the Post model
#         serializer.save(updated_by=self.request.user.id)

# class PostListView(generics.ListAPIView):
#     queryset = Post.objects.annotate(num_likes=Count('like')).all()
#     serializer_class = PostSerializer

# class LikeListCreateView(generics.ListCreateAPIView):
#     queryset = Like.objects.all()
#     serializer_class = LikeSerializer

# class LikeRetrieveUpdateView(generics.RetrieveUpdateAPIView):
#     queryset = Like.objects.all()
#     serializer_class = LikeSerializer

class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.annotate(num_likes=Count('like')).all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.annotate(num_likes=Count('like')).all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class LikeCreateView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

class LikeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
