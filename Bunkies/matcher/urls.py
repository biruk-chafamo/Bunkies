from django.urls import path, include
from .views import *

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'connection', ConnectionViewSet, basename='connection')
# router.register(r'equbjoinrequests', EqubJoinRequestViewSet, basename='equbjoinrequest')
# router.register(r'equbinviterequests', EqubInviteRequestViewSet, basename='equbinviterequest')
# router.register(r'friendrequests', FriendRequestViewSet, basename='friendrequest')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
