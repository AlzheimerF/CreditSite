from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user.views import ProfileViewSet, InfoViewSet

router = DefaultRouter()
router.register('', InfoViewSet, basename='info_user')

urlpatterns = router.urls