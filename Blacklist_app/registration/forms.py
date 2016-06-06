
# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    
    password1 = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmation du mot de passe", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username', 'email')
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                "Les deux mots de passes ne correspondent pas.",
                code='password_mismatch',
            )
        return password2
