from django import forms

class ContactForm(forms.Form):
    name=forms.CharField(max_length=255)
    email=forms.EmailField(max_length=255)
    content=forms.CharField(widget=forms.Textarea)