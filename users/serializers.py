from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
import django.contrib.auth.password_validation as validators


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name")

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required = True,validators=[UniqueValidator(queryset=User.objects.all())])
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
        validators.validate_password(password)
        return data
