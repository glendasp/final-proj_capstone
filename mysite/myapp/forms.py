__author__ = 'Glenda Pinho'
from django import forms
from .models import SignUp, ContactForm


class ContactForm(forms.Form):
    full_name = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    message = forms.CharField(required=False)


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
