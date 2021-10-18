from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User

from users.serializers import RegisterSerializer

class UserRegisterView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
    queryset = User.objects.all()

