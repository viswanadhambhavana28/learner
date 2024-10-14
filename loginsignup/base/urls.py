from django.urls import path,include
from .views import authview

urlpatterns = [
  path("signup/", authview, name="authview"),
  path("accounts/", include("django.contrib.auth.urls")),
]