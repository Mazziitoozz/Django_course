from django.urls import path
from app_3 import views

urlpatterns = [
    path("sign_in ", views.user, name="user"),
]