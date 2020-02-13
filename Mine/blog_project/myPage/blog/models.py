from django.db import models
from django.utils import timezone #add time
from django.urls import reverse 
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User',related_name='Post',on_delete=models.CASCADE) # When the user login in the page this is his name
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now) #add time now hen you post
    published_date = models.DateTimeField(blank=True,null=True) #Note that this is different than null. null is purely database-related, whereas blank is 
                                                                # validation-related. If a field has blank=True, form validation will allow entry of an empty value.
                                                                #  If a field has blank=False, the field will be required.
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)
   
    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.pk}) # when you click in save new post you go to this direction 
        #You create models for your website. When a new instance is made for a model, django must know where to go when a new post is created or a new instance is created.
        
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('Post', related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("blog:post_list")

    def __str__(self):
        return self.text
