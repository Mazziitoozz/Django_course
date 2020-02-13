from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    mydic={"name":"Juan is in the street"}
    return render(request,"AppTest/index.htm",context=mydic)

def help(request):
    helpdict = {'help_insert':"Help page"}
    return render(request,"AppTest/help.htm",context=helpdict)