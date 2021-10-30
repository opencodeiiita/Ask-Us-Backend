from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from django.contrib.auth import logout
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from users.serializers import RegisterSerializer,UserSerializer,ChangePasswordSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import UpdateAPIView
from qna.serializers import QuestionSerializer
from qna.models import Question
from qna.serializers import AnswerSerializer
from qna.models import Answer

class UserRegisterView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data=dict(serializer.data)
        data["token"]=Token.objects.get(user=data["id"]).key
        return Response(data,status=status.HTTP_201_CREATED, headers=headers)

class UserLogoutView(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
        return Response(status=status.HTTP_200_OK)

class ListUsers(APIView):
    def get(self, request, format=None):
         user=UserSerializer(User.objects.all().filter(is_staff=False),many=True)
         return Response(user.data,status=status.HTTP_200_OK)

class ChangePasswordView(UpdateAPIView):
        serializer_class = ChangePasswordSerializer
        model = User
        def update(self, request, *args, **kwargs):
            self.object = self.request.user
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                response = {
                    'message': 'Password updated successfully',
                }
                return Response(status= status.HTTP_200_OK, data = response)
            return Response(status=status.HTTP_400_BAD_REQUEST)

class ListQuestionsByUser(APIView):
    def get(self, request, *args, **kwargs):
        _username= kwargs.get("username")
        user=User.objects.get(username=_username)
        _id=user.id
        data = QuestionSerializer(Question.objects.all().filter(author=_id).order_by('-date_posted'), many=True).data
        return Response(data,status=status.HTTP_200_OK)

class ListAnswersByUser(APIView):
    def get(self, request, *args, **kwargs):
        _username= kwargs.get("username")
        user=User.objects.get(username=_username)
        _id=user.id
        data = AnswerSerializer(Answer.objects.all().filter(author=_id).order_by('-date_posted'), many=True).data
        return Response(data,status=status.HTTP_200_OK)

class UserUpdateView(UpdateAPIView):
    def put(self, request, *args, kwargs):
        _username= kwargs.get("username")
        user=User.objects.get(username=_username)
        data = request.data
        user_serializer = UserSerializer(user, data=data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, *args, kwargs):
        _username= kwargs.get("username")
        user=User.objects.get(username=_username)
        data = request.data
        user_serializer = UserSerializer(user, data=data, partial=True)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data,status=status.HTTP_200_OK)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
