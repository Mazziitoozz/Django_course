from django.db import models
from django.contrib import auth
from django.utils import timezone

# Create your models here.
'''PermissionsMixin
This is an abstract model you can include in the class hierarchy 
for your user model, giving you all the methods and database fields necessary to support Django’s permission model.'''
class User(auth.models.User,auth.models.PermissionsMixin):
    def __str__(self):
        return"@{}".format(self.username) # from model user take object username and put inside @

