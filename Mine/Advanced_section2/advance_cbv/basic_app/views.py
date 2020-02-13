from django.shortcuts import render
from django.urls import reverse_lazy 
from django.views.generic import View,TemplateView,ListView,DetailView 
from django.views.generic.edit import CreateView,UpdateView,DeleteView
# from django.http import HttpResponse
from . import models

'''We usually do that URL--> path("", views.index, name="index"),'''
# Create your views here.
# def index(request):
#     return render(request,"index.htm")

'''Now we are gona change in url too, from basic_app.views import CBView.     path("", CBView.as_view(), name="CBVIew")'''
# class CBView(View):
#     def get(self,request):
#         return HttpResponse("Class Base View is good")

class IndexView(TemplateView):
    template_name = 'index.htm' # Because i dont have a folder inside templates if not i would have had basic_app/index.htm

'''Function to inject text in html code, using dicts'''
    # def get_context_data(self,**kwargs): #keyword arguemnts-> function(name="one",age=27) or *arg in order to arg
    #     context = super().get_context_data(**kwargs)
    #     context['injectme'] = 'Basic Injection'
    #     return context

class SchoolListView(ListView):
    context_object_name = 'schools'#easy to read in school.list.htm
    model = models.School
    template_name = "basic_app/school_list.htm" 
    # school_list

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail' #useful to use in htm
    model = models.School
    template_name = "basic_app/school_detail.htm"

class SchoolCreateView(CreateView):
    model = models.School
    fields = ('name','principal','location')
    template_name = "basic_app/school_form.htm" # It is not necessary to put if your document is _form.html because is by default 

class SchoolUpdateView(UpdateView):
    model = models.School
    fields = ('name','principal')
    template_name = "basic_app/school_form.htm"

class SchoolDeleteView(DeleteView):
    model = models.School
    template_name = "basic_app/school_delete.htm"
    success_url = reverse_lazy("basic_app:list")
    


   
