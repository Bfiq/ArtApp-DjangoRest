from .views import UserRegistration, BoardsView, PinView, BoardPinView, TagView
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
    path('pins/', PinView.as_view(), name='pins'),
    path('pins/<int:pk>/', PinView.as_view(), name='pin-detail'),
    path('board-pin/', BoardPinView.as_view(), name='boards-Pins'),
    path('board-pin/<int:pk>/', BoardPinView.as_view(), name='boards-Pins-detail'),
    path('tag/', TagView.as_view(), name='tags'),
    path('tag/<int:pk>/', TagView.as_view(), name='tag-detail'),
    path('pin-tag/', TagView.as_view(), name='pin-tag'),
    path('pin-tag/<int:pk>/', TagView.as_view(), name='pin-tag-detail'),
]
