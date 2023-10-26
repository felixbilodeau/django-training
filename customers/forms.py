from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

from .models import Customer

User = get_user_model()


class CustomerCreateForm(forms.Form):
    first_name = forms.CharField(max_length=150, label='First Name')
    last_name = forms.CharField(max_length=150, label='Last Name')
    email = forms.EmailField(label='Email')
    username = forms.CharField(max_length=150, label='Username')
    password = forms.CharField(max_length=128, widget=forms.PasswordInput(), label='Password')
    password_confirm = forms.CharField(max_length=128, widget=forms.PasswordInput(), label='Confirm Password')

    def clean_email(self):
        email = self.cleaned_data['email']
        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            raise ValidationError(message='User with this email already exists', code='duplicate')
        return email

    def clean(self):
        output = super().clean()
        if self.cleaned_data['password'] != self.cleaned_data['password_confirm']:
            self.add_error('password', ValidationError(message='Passwords do not match', code='invalid'))
            self.add_error('password_confirm', ValidationError(message='Passwords do not match', code='invalid'))
        return output
    
    def save(self):
        if not hasattr(self, 'cleaned_data'):
            raise ValidationError(message='Form not validated yet!', code='not_validated')
        
        user = User.objects.create(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email'],
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )

        customer = Customer.objects.create(user=user)
        return customer
    

class CustomerUpdateForm(forms.Form):
    first_name = forms.CharField(max_length=150, label='First Name')
    last_name = forms.CharField(max_length=150, label='Last Name')
    email = forms.EmailField(label='Email')
    username = forms.CharField(max_length=150, label='Username')

    def __init__(self, data, *args, instance=None, **kwargs):
        super().__init__(data, *args, **kwargs)
        if not instance:
            raise ValueError('Update form requires an instance to be provided')
        
        self.instance = instance
        self.initial = {
            'first_name': instance.user.first_name,
            'last_name': instance.user.last_name,
            'email': instance.user.email,
            'username': instance.user.username,
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        user_qs = User.objects.filter(email=email).exclude(pk=self.instance.pk)
        if user_qs.exists():
            raise ValidationError(message='User with this email already exists', code='duplicate')
        return email
    

    def save(self):
        user = self.instance.user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']
        user.save()
        return self.instance
