from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token
from.views import AuthApView
urlpatterns = [
    path(r'jwt/', AuthApView.as_view(),name='auth'),
    path(r'jwt/refresh/', refresh_jwt_token),
]
