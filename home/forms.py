from django import forms

class NewMessageForm(forms.Form):
    name = forms.CharField(max_length=200)
    message = forms.CharField(max_length=200)