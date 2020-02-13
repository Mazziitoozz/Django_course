from django.db import models
from django.urls import reverse 

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

# No URL to redirect to.  Either provide a url or define a get_absolute_url method on the Model.
    def get_absolute_url(self):
        return reverse("basic_app:detail", kwargs={"pk": self.pk})

class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,related_name='students',on_delete=models.CASCADE)# related name is the name that you can se in Django  After Basic_app-->Studetns

    def __str__(self):
        return self.name