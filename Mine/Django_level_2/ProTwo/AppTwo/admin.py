from django.contrib import admin
from AppTwo.models import * #import models to register and after that you can create a superuser 
# Register your models here.

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)