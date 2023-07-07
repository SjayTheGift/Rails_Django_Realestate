from django.contrib.auth import get_user_model
from rest_framework import generics, mixins, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView 
from rest_framework_simplejwt.tokens import RefreshToken

User =  get_user_model()

from .serializers import (
    LogInSerializer, 
    UserCreateSerializer,
    LogoutSerializer
)

class SignUpView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer

    def post(self, request, *args, **kwargs):
        print(request.POST.get('email', None))
        return self.create(request, *args, **kwargs)


class LogInView(TokenObtainPairView): # new
    serializer_class = LogInSerializer


class LogoutView(generics.CreateAPIView):
    serializer_class = LogoutSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)



# class LogoutView(APIView):
#     permission_classes = (permissions.IsAuthenticated,)

#     def post(self, request):
#         try:
#             refresh_token = request.data["refresh_token"]
#             print(refresh_token)
#             token = RefreshToken(refresh_token)
#             token.blacklist()
#             return Response(status=status.HTTP_205_RESET_CONTENT)
#         except Exception as e:
#             return Response(status=status.HTTP_400_BAD_REQUEST)