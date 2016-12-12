__author__ = 'Glenda Pinho'
from django import forms
from .models import SignUp


class ContactForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()


    # Validate email if it has .edu
    def clean_email(self):
        # run into all the validations .......
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain, extension = provider.split('.')
        # if not domain ==  "USC":
        #     raise forms.ValidationError("Please make sure you use your college email")
        if not extension == "edu":
            raise forms.ValidationError("Please use a valid .EDU email address")
        return email


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email']

    def clean_email(self):
        # run into all the validations .......
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain, extension = provider.split('.')
        # if not domain ==  "USC":
        #     raise forms.ValidationError("Please make sure you use your college email")
        if not extension == "edu":
            raise forms.ValidationError("Please use a valid .EDU email address")
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        #todo validation code
        return full_name