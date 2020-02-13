from django.shortcuts import render
from django.http import HttpResponse
#from app_3.models import *
from app_3.forms import NewUserForm
# Create your views here.

def index(request):
    return render(request,"app_3/index.htm")

def user(request):
    form = NewUserForm()

    if request.method == "POST": 
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR FORM INVALID")
    return render(request,"app_3/users.htm",{"form":form})