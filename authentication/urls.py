from django.urls import path

from .views import *


urlpatterns = [
    path('registration/', RegistrationAPIView.as_view(), name='registration'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('update/', UserRetrieveUpdateAPIView.as_view(), name='update'),
]