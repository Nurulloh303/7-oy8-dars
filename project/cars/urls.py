from django.urls import path
from .views import CarAPIView, CarCreateAPIView, OwnerCreateAPIView, OwnerAPIView

urlpatterns = [
    path('cars/', CarAPIView.as_view()),
    path('cars/<int:pk>/', CarAPIView.as_view()),
    path('cars/create/', CarCreateAPIView.as_view()),
    path('owners/', OwnerAPIView.as_view()),
    path('owners/<int:pk>/', OwnerAPIView.as_view()),
    path('owners/create/', OwnerCreateAPIView.as_view()),
]