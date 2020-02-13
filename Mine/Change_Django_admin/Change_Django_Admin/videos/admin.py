from django.contrib import admin
from . import models
# Register your models here.

# By default Django put the date in the Admin Web in the order that you add,    
    # title = models.CharField(max_length=256)
    # length = models.PositiveIntegerField()
    # release_year = models.PositiveIntegerField() 
# If you wan to change the order you must to create a class and put hte order of the fields.
# when you register the model, you should do the same with the class
class MovieAdmin(admin.ModelAdmin):

    fields = ['release_year','title','length']

    search_fields = ["title","length"] # IF you want to add a searcher

    list_filter = ['release_year','length'] # Just in case that you want to add a filters

    list_display = ['title','release_year','length'] # Just in case that you want to add  more colums to the movies
   
    list_editable = ['length'] #if you want to change the things instead of clicking

admin.site.register(models.Customer)
admin.site.register(models.Movie,MovieAdmin)