from django.urls import path
from authentication.api.views.views import RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView

urlpatterns = [
    path('register', RegistrationAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('update', UserRetrieveUpdateAPIView.as_view())
]
