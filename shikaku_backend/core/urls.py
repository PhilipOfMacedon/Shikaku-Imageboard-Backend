from django.urls import path, include
from . import views

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('login/', views.ObtainTokenView.as_view(), name='login'),
]