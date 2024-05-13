from django import forms

class ContactUsForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField()
    