"""Accounts views module."""
from rest_framework import generics, mixins, permissions, status
from rest_framework.response import Response

from accounts.models import AppUser
from accounts.serializers import AppUserSerializer


class AppUser(mixins.CreateModelMixin, generics.GenericAPIView):
    """AppUser new class based view."""

    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        """Post method for creating new user."""
        data = request.data.copy()
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            self.object = serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
                headers=headers
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
