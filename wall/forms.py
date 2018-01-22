from django import forms

class UserPostForm(forms.Form):

    text =  forms.TextField(max_lenght=400)
    url =   forms.URLField()
    image = forms.ImageField()

