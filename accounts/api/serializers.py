from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler=api_settings.JWT_RESPONSE_PAYLOAD_HANDLER
User=get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    # password=serializers.CharField(style={'input_type':'password'},write_only=True)
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    token=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=User
        fields=[
            'username',
            'email',
            'password',
            'password2',
            'token'
        ]
        extra_kwargs={'password':{'write_only':True}}
    def get_token(self,obj):
        user=obj
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token
    def validate_email(self,value):
        qs = User.objects.filter(email__iexact=value)
        if qs.exists():
            raise serializers.ValidationError('User with this email already exist')
        return value
    def validate_username(self,value):
        qs=User.objects.filter(username__iexact=value)
        if qs.exists():
            raise serializers.ValidationError('User with this Username already exist')

        return value

    def validate(self, data):
        pw=data.get('password')
        pw2=data.get('password2')
        if pw!=pw2:
            raise serializers.ValidationError('passwords must match')
        return data
    def create(self, validated_data):
        print(validated_data)
        user_obj=User(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
        )
        user_obj.set_password(validated_data.get('password'))
        user_obj.save()
        return user_obj
