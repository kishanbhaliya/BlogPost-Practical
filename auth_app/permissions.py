from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed
from auth_app.models import User
from django.conf import settings
import jwt
from rest_framework import permissions


def decode_token(token):
    try:
        # Replace 'your_secret_key' with the actual secret key used to sign the tokens
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Token has expired.')
    except jwt.InvalidTokenError:
        raise AuthenticationFailed('Invalid token.')



class UserAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        # Get the 'Authorization' header from the request
        auth_header = request.headers.get('Authorization')

        if not auth_header:
            # If 'Authorization' header is not present, return None (not authenticated)
            return None

        # Split the 'Authorization' header value to get the token
        try:
            _, token = auth_header.split()
        except ValueError:
            # If the header format is invalid, raise AuthenticationFailed
            raise AuthenticationFailed('Invalid token header.')

        # Implement your custom logic to validate the token and get the user
        try:
            payload = decode_token(token)
            user = User.objects.get(pk=payload['user_id'])
            return (user, None)
        except User.DoesNotExist:
            # If the user doesn't exist, return None (not authenticated)
            return None

class AllowAnyReadOnly(AllowAny):
    def has_permission(self, request, view):
        if request.method in ['GET']:
            return True
        return False

