from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions,generics
from django.contrib.auth import authenticate,get_user_model

# Create your views here.
from rest_framework_jwt.settings import api_settings
from .serializers import UserRegisterSerializer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler=api_settings.JWT_RESPONSE_PAYLOAD_HANDLER
User=get_user_model()
class AuthApView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request, *args, **kwargs):
        print(request.user)
        if request.user.is_authenticated:
            return Response({'detail': 'you are already authenticated'},status=404)
        data=request.data
        username=data.get('username')
        password=data.get('password')
        user=authenticate(username=username,password=password)

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        response=jwt_response_payload_handler(payload,token,user,request=request)

        return Response(response)

class RegisterApiView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]