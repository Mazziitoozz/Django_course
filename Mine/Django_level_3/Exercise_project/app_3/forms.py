from django import forms
from app_3.models import Users

class NewUserForm(forms.ModelForm):
    #It is cool than forms in basicforms
    class Meta():
        model = Users
        fields = "__all__"