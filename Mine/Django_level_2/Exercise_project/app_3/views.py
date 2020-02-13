from django.shortcuts import render
from django.http import HttpResponse
from app_3.models import *
# Create your views here.

def index(request):
    return render(request,"app_3/index.htm")

def user(request):
    users_list = Users.objects.order_by("first_name")
    users_dict = {"Users":users_list}
    return render(request,"app_3/users.htm",context=users_dict)
    