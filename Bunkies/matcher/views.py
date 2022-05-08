from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.response import Response

from .serializers import *
from .models import *
from .permissions import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')

    def get_permissions(self):
        if self.request.method in ['GET', 'POST']:
            return [permissions.AllowAny()]
        else:
            return [permissions.DjangoObjectPermissions()]

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE', 'POST']:
            return RegisterUserSerializer
        # if self.request.method in ['PUT']:
        #     return UserSerializer
        return ListUserSerializer


# class ConnectionViewSet(viewsets.ModelViewSet):
class ConnectionViewSet(AuthenticatedAndObjectPermissionMixin, viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        received_connections = Connection.objects.filter(receiver=user)
        sent_connections = Connection.objects.filter(sender=user)
        return received_connections | sent_connections

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method in ['PUT', 'PATCH']:
            return AcceptConnectionRequestSerializer
        else:
            return ConnectionRequestSerializer

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
