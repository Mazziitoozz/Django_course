from django.urls import path,repath
from app_test import views

urlpatterns = [
    path("", views.help, name="help"),
    repath(r'^api-auth/', include('rest_framework.urls'))
]