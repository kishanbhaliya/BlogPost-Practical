from django.urls import path
from blog_app.views import (
    PostListCreateView,
    PostRetrieveUpdateDeleteView,
    LikeListCreateView,
    LikeRetrieveUpdateView,
)

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<uuid:pk>/', PostRetrieveUpdateDeleteView.as_view(), name='post-retrieve-update-delete'),
    path('likes/', LikeListCreateView.as_view(), name='like-list-create'),
    path('likes/<uuid:pk>/', LikeRetrieveUpdateView.as_view(), name='like-retrieve-update'),
]