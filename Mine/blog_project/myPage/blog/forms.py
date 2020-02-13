from django import forms
from django.contrib.auth.models import User
from blog.models import Post,Comment

class Post_form(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('author','title','text')
        widgets ={
            'title':forms.TextInput(attrs={'class':'textinputclass'}), # is our own class
            'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea '}) # postcontent is our own class
        }
class Comment_form(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('author','text')
        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea '}) # postcontent is our own class


        }

