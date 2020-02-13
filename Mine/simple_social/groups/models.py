from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify #Converts a string to a URL slug by:  slugify(' Joel is a slug ') -->'joel-is-a-slug'
# from accounts.models import User

# pip install misaka
#import misaka

from django.contrib.auth import get_user_model

User = get_user_model() #create an object called User

# https://docs.djangoproject.com/en/2.0/howto/custom-template-tags/#inclusion-tags
# This is for the in_group_members check template tag
from django import template
register = template.Library()

class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User,through="GroupMember")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name) 
        #self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("groups:single", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["name"]

class GroupMember(models.Model):
    group = models.ForeignKey(Group,related_name='memberships',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='user_groups',on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

        '''Model metadata is “anything that’s not a field”, such as ordering options (ordering), database table name (db_table),
         or human-readable singular and plural names (verbose_name and verbose_name_plural). None are required, and adding class Meta to a model is completely optional.
         Also you have a lot of thing to edit the db. Remember that django when you create an app startapp groups, the name os you table is: group_nameClass'''
    class Meta:
        unique_together = ("group","user") #Sets of field names that, taken together, must be unique: