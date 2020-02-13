from django.urls import path
from basic_app import views

# TEMPLATE TAGGING
app_name = "basic_app" # necessary to put if you want to call in html app_name: "name of the app"

urlpatterns = [
    path("other/", views.other, name="other"),
    path("relative/", views.relative_url_templates, name="relative_url_templates"),
]