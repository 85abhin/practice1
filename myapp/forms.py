from django import forms
from django.contrib.auth.forms import *
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth import password_validation
from .models import Customer

class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'email': 'Email'}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password=forms.CharField(label=_("password"),strip=False,widget=forms.PasswordInput(attrs={'class':'form-control','autocomplete':'current-password'}))
    

class PasswordChange(PasswordChangeForm):
  old_password=forms.CharField(label=_("old password"),strip=False,widget=forms.PasswordInput(attrs={'class':'form-control','autocomplete':'current-password'}))
  new_password1=forms.CharField(label=_("new password"),strip=False,widget=forms.PasswordInput(attrs={'class':'form-control','autocomplete':'new-password'}),help_text=password_validation.password_validators_help_text_html)
  new_password2=forms.CharField(label=_("confirm new password"),strip=False,widget=forms.PasswordInput(attrs={'class':'form-control','autocomplete':'new-password'}))


class Mypasswordrestform(PasswordResetForm):
    email=forms.EmailField(label=_('Your Email'),max_length=254,widget=forms.EmailInput(attrs={'autocomplete':'email','class':'form-control'}))
    
class Mysetpasswordform(SetPasswordForm):
      new_password1=forms.CharField(label=_("new password"),strip=False,widget=forms.PasswordInput(attrs={'class':'form-control','autocomplete':'new-password'}),help_text=password_validation.password_validators_help_text_html)
      new_password2=forms.CharField(label=_("confirm new password"),strip=False,widget=forms.PasswordInput(attrs={'class':'form-control','autocomplete':'new-password'}))

class CustomerAddressForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['name','locality','city','zipcode','state']
        widgets={'name':forms.TextInput(attrs={'class':'form-control'}),
                'locality':forms.TextInput(attrs={'class':'form-control'}),
                 'city':forms.TextInput(attrs={'class':'form-control'}),
                 'zipcode':forms.NumberInput(attrs={'class':'form-control'}),
                 'state':forms.Select(attrs={'class':'form-control'})                                                               
                }


