from rest_framework import serializers
from .models import Answer, Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required = True)
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
