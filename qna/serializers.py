from rest_framework.serializers import ModelSerializer
from .models import Answer, Question


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"

class RegisterSerializer(ModelSerializer):
    email = ModelSerializer.CharField(required = True)
    password = ModelSerializer.CharField(required = True,Write_only = True)
    password2 = ModelSerializer.Field(required = True,Write_only = True)

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
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password':'passwords must match'})
    return data
