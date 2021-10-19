from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from rest_framework import permissions
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from users.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

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

