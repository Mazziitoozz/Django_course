import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE","Exercise_project.settings")

import django
django.setup()

import random
from app_3.models import Users
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):

        fake_name = fakegen.name().split() # fake name is randon name Juan Perez

        fake_firstname = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()

        #New Entry User
        user = Users.objects.get_or_create(first_name=fake_firstname,
                                            last_name=fake_last_name,
                                            email=fake_email)[0]
if __name__ =="__main__":
    print("populating script!")
    populate(20)
    print("populating complete")
