import djoser
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from api.views import TransportViewSet, TourViewSet, BookingViewSet

router = DefaultRouter()
router.register('transport',TransportViewSet)
router.register('tour',TourViewSet)
router.register('booking',BookingViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
