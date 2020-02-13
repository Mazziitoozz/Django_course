from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.urls import reverse_lazy
#Models
from blog.models import Post, Comment
#Forms
from blog.forms import Post_form,Comment_form
#Decorators
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# CBV
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.

class AboutView(TemplateView):
        template_name = 'blog/about.html' # Because i dont have a folder inside templates if not i would have had basic_app/index.html

class PostListView(ListView):
    model = Post
    #template_name = "blog/post_list.html" 
    #content_type=post_list
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by("-published_date") # take post model,all objects and filter. Grab publish date,lte= last then or equal to the current time and order. - means descend order
                                                                                                        # SELECT * from post where published_date <= cureent date

class PostDetailView(DetailView):
    model = Post

# LoginRequiredMixin is the same that @login_required bbut in CBV.If a view is using this mixin, all requests by non-authenticated users will be redirected to the login page  (If the user isn’t 
# logged in, redirect to settings.LOGIN_URL),or shown an HTTP 403 Forbidden error, depending on the raise_exception parameter.
class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = "/login/"
    redirect_field_name = "blog/post_detail.html"
    #template_name = "blog/post_list.html" 
    form_class = Post_form
    model = Post

class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = "/login/"
    redirect_field_name = "blog/post_detail.html"

    form_class = Post_form
    model = Post
    #template_name = "TEMPLATE_NAME"

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy("blog:post_list")
    #template_name = "TEMPLATE_NAME"

class DraftListView(LoginRequiredMixin,ListView):
    login_url = "/login/"
    redirect_field_name = "blog/post_list.html"
    
    model=Post
    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by("-created_date") # take post model,all objects and filter. Grab publish date,lte= last then or equal to the current time and order. - means descend order

#############
# Functions which need pk
###########
@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk) #It is a shortcut if the object Post doesnt exist 
    '''try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")'''
    post.publish() # execute publish function in class Post. Important put put in lowercase because is post = Post.objects.get(pk=post_id) 
    return redirect("blog:post_detail",pk=pk)

@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == "POST": # someone fill the form 
        form = Comment_form(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("blog:post_detail",pk=post.pk)
    else:
        form = Comment_form()
    return render(request,"blog/comment_form.html",{'form':form})

@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect("blog:post_detail",pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect("blog:post_detail",pk=post_pk)


