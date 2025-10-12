from django.urls import path
from .views import  ColorDetailAPIView, OwnerDetailAPIView, CarApiView
from rest_framework.routers import SimpleRouter, DefaultRouter

router = DefaultRouter()
router.register('cars', CarApiView, basename='car')

urlpatterns = [
    path('owners/', OwnerDetailAPIView.as_view()),
]

urlpatterns += router.urls