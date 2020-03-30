from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import CustomUser
from .seralizer import CustomUserSeralizer


class CustomUserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CustomUserSeralizer
    queryset = CustomUser.objects.all()

    def create(self, request, *args, **kwargs):

        serializer:CustomUserSeralizer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=CustomUser()
        user.email=serializer.validated_data['email']
        user.set_password(serializer.validated_data['password'])
        user.username=serializer.validated_data['username']
        user.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)