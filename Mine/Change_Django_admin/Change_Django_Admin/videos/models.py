from django.db import models

# Create your models here.

class Movie(models.Model):
    # If you want to change the order you can do that  in the admin.py
    title = models.CharField(max_length=256)
    length = models.PositiveIntegerField()
    release_year = models.PositiveIntegerField()

    # In the Admin if you don give string representation you only can see Movie Object(1), Movie Object(2)... now you can see the title
    def __str__(self):
        return self.title

class Customer(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    phone = models.PositiveIntegerField()

    # In the Admin if you don give string representation you only can see Customer Object(1), Customer Object(2)... now you can see the name and surname
    def __str__(self):
        return self.first_name + "  "+ self.last_name