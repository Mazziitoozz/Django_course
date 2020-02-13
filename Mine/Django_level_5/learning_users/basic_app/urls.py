from django.urls import path,include
from basic_app import views

# TEMPLATE TAGGING
app_name = "basic_app" # necessary to put if you want to call in html app_name: "name of the app"
urlpatterns = [
    path("register/", views.register, name="register"),
    path("user_login/", views.user_login, name="user_login"),


]