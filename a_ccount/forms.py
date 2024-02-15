from django import forms
from django.contrib.auth.models import User
from .models import Profile
# from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.conf import settings


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_repeat = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

    def clean_password_repeat(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password_repeat']:
            raise ValidationError("Both fields should have the same vlaues!")
        return cd['password_repeat']

    def clean_email(self):
        cd = self.cleaned_data
        if User.objects.filter(email=cd['email']).exists():
            raise ValidationError("Email already exists")
        return cd['email']


class UserEditForm(forms.ModelForm):
    class Meta:
        # model = settings.AUTH_USER_MODEL
        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean_email(self):
        """we exclude the current user because its current email crashes if he uses that again"""
        cd = self.cleaned_data
        query_set = User.objects.exclude(id=self.instance.id)
        if query_set.filter(email=cd['email']).exists():
            raise ValidationError("Email already exists")
        return cd['email']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'image']
