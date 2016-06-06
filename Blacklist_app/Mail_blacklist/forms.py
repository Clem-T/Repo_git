# -*- coding: utf-8 -*-
from django import forms
from Mail_blacklist.models import Email


class EmailForm(forms.ModelForm):
    
    class Meta:
        model = Email
        exclude = ('user_id',)
        
class FileForm(forms.Form):
    
    file = forms.FileField()
