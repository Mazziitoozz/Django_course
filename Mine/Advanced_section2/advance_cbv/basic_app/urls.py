from django.urls import path,include,re_path
from basic_app.views import SchoolListView,SchoolDetailView,SchoolCreateView,SchoolUpdateView,SchoolDeleteView

app_name = "basic_app"

urlpatterns = [
    path("", SchoolListView.as_view(), name="list"), #name is usefull becasuse if you see the bsae.htm you can see {% basic_app: list %}
    path("create/", SchoolCreateView.as_view(), name="create"),     
    re_path(r'^(?P<pk>[-\w]+)/$', SchoolDetailView.as_view(), name="detail"), # regular expresion. When you click in a school you need 
                                                                       # his pk--> primary key which is a number \w any single character. + onde more.
                                                                        # When i call detail i need to send pk
    re_path(r'^update/(?P<pk>[-\w]+)/$', SchoolUpdateView.as_view(), name="update"), 
    re_path(r'^delete/(?P<pk>[-\w]+)/$', SchoolDeleteView.as_view(), name="delete"), 

]