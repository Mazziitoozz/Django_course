from django.urls import path,include,re_path
from blog.views import *#AboutView,PostListView,PostDetailView,CreatePostView,PostDeleteView,DraftListView,add_comment_to_post,comment_approve,comment_remove
from blog import views
# TEMPLATE TAGGING
app_name = "blog" # necessary to put if you want to call in html app_name: "name of the app"

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("about/", AboutView.as_view(), name="about"),
    re_path(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view(), name="post_detail"), # regular expresion. When you click in a school you need 
                                                                       # his pk--> primary key which is a number \d any digit. + onde more.
                                                                        # When i call detail i need to send pk
    path("post/new/", CreatePostView.as_view(), name="post_new"),
    re_path(r'^post/(?P<pk>\d+)/edit/$', PostUpdateView.as_view(), name="post_edit"), 
    path("drafts/", DraftListView.as_view(), name="post_draft_list"), 

    re_path(r'^delete/(?P<pk>\d+)/remove/$', PostDeleteView.as_view(), name="post_remove"), 
    re_path(r'^post/(?P<pk>\d+)/comment/$',views.add_comment_to_post, name="add_comment_to_post"), 
    re_path(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name="post_publish"), 
    re_path(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name="comment_approve"), 
    re_path(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name="comment_remove"), 
 







]



