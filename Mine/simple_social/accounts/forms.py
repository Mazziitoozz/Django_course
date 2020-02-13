from django.contrib.auth import get_user_model #This method will return the currently active user model

from django.contrib.auth.forms import  UserCreationForm #A ModelForm for creating a new user.It has three fields: username (from the user model), password1, and password2.
# It verifies that password1 and password2 match, validates the password using validate_password(), and sets the user’s password using set_password().

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username","email","password1","password2") #this fields are inside the user
        model = get_user_model()

    ''' __init__()is what is called as a constructor in other OOP,The basic idea is that it is a special method which is automatically called when an object of that Class is created  https://stackoverflow.com/a/625098 '''
    
    def __init__(self,*args,**kwargs):#*(whatever you want to call)=arguments **(whatever you want to call) keywords
        super().__init__(*args,**kwargs) # super() refers to a superclass imagine you have class Person and class Student(Person) , ypu can use Person.__init__ or super().__init__
        self.fields['username'].label="Display Name"
        self.fields["email"].label = "Email Address"