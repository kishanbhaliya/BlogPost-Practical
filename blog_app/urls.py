from django.urls import path
from blog_app.views import (
    # PostListCreateView,
    PostCreateView,
    PostListView,
    PostDetailView,
    # PostRetrieveUpdateDeleteView,
    LikeCreateView,
    LikeDetailView,
)

urlpatterns = [
    # path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/', PostCreateView.as_view(), name='post_create'),
    path('posts/list/', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    # path('posts/<uuid:pk>/', PostRetrieveUpdateDeleteView.as_view(), name='post-retrieve-update-delete'),
    path('likes/', LikeCreateView.as_view(), name='like-list-create'),
    path('likes/<uuid:pk>/', LikeDetailView.as_view(), name='like-retrieve-update'),
]