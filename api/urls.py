from .views import UserRegistration, BoardsView
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegistration.as_view(), name='user_register'),
    path('boards/', BoardsView.as_view(), name='boards'),
    path('boards/<int:pk>/', BoardsView.as_view(), name='board-detail'),
]
