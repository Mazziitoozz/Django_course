from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import *
# Create your views here.
def index(request):    
    webpages_list = AccessRecord.objects.order_by("date") # get webpage list and order
    date_dict = {"access_records":webpages_list,'insert_me':"Hello I am coming from App_2"}    # You create the variable that you are gonna insert in html
 
    return render(request,'App_2/index.htm',context=date_dict)