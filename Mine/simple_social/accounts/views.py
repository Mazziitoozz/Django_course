from django.shortcuts import render
from django.urls import reverse_lazy # we use in case that someone is logout or login where did should actually go
from django.views.generic import CreateView
from . import forms
# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')#I have to use reverse_lazy() when I want to reverse to an URL that has not been loaded. So when I create a CBV and state a success_url, I use reversy_lazy. 
    template_name = "accounts/signup.html"