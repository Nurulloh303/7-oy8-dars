from django.urls import path
from .views import CarDetailAPIView, ColorDetailAPIView, OwnerDetailAPIView, CarApiView

urlpatterns = [
    path('cars/', CarApiView.as_view()),
    path('cars/<int:pk>/', CarDetailAPIView.as_view()),
    path('owners/', OwnerDetailAPIView.as_view()),
]