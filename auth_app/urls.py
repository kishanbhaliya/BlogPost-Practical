from django.urls import path
from auth_app.views import (
    UserRegistrationView,
    user_login,
    UserListView,
    UserRetrieveUpdateDestroyView,

)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', user_login, name='user-login'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<uuid:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-retrieve-update-destroy'),
]