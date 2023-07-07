from django.urls import path

from .views import (
    LogInView, 
    LogoutView,
    SignUpView 
    )

urlpatterns = [
    path('api/user/login/', LogInView.as_view(), name='login'),
    path('api/user/logout/', LogoutView.as_view(), name='logout'),
    path('api/user/register/', SignUpView.as_view(), name='register-user'),
]
