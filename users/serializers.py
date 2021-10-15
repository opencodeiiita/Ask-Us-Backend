from typing_extensions import Required
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name")

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required = True)
    password = serializers.CharField(required = True,write_only = True)
    password2 = serializers.CharField(required = True,write_only = True)

    class Meta:
        model = User
        fields = ['id','username','password','password2','email','first_name','last_name']


    def create(self,validated_data):
        user = User.objects.create_user(
                username=validated_data['username'],
                password=validated_data['password'],
                email = validated_data['email']
            )
        return user

    def validate(self,data):
        password = data['password']
        password2 = data['password2']
        if password != password2:
            raise serializers.ValidationError({'password':'passwords must match'})
        return data

    def validate_email(self,data):
        email_lower = data['email'].lower()
        if User.objects.filter(email__iexact=email_lower).exists():
            raise serializers.ValidationError({'email':'Email already exists'})
        return email_lower