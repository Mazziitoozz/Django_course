from django.urls import path
from app_3 import views

urlpatterns = [
    path("all_user", views.user, name="user"),
]