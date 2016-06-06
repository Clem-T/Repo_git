# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from registration.forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def register(request):
    if request.method=='POST':
        form = UserForm(request.POST, instance=User())
        if form.is_valid():
            user=form.save()
            user.set_password(form.cleaned_data["password2"])
            user.save()
            
            #trying to authenticate user
            auth_user = authenticate(username=user.username, 
                                     password=form.cleaned_data["password2"])
            if auth_user:
                login(request,auth_user)
                return redirect("Mail_blacklist.views.home")
            
    else:
        form=UserForm(instance=User())
    
    return render(request, 'registration/register.html', locals() )
