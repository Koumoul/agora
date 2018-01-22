from django import forms

class UserPostForm(forms.Form):

    text =  forms.CharField(max_length=400)

