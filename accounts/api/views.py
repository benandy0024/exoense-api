from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate,get_user_model
# Create your views here.
jwt_payload_handler=api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler=api_settings.JWT_DECODE_HANDLER

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
        payload=jwt_payload_handler(user)
        token=jwt_encode_handler(payload)
        print(user)
        return Response({'token':token})

