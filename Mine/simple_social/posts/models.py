from django.db import models
from django.conf import settings
from django.urls import reverse

# pip install misaka
#import misaka

from groups.models import Group

from django.contrib.auth import get_user_model
User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, related_name="posts",null=True, blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        #self.message_html= misaka.html(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "posts:single",
            kwargs={
                "username": self.user.username,
                "pk": self.pk
            }
        )# when you click in save new post you go to this direction 
        #You create models for your website. When a new instance is made for a model, django must know where to go when a new post is created or a new instance is created.

    class Meta:
        ordering = ["-created_at"]
        unique_together = ["user", "message"]
