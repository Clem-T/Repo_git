# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Mail_blacklist.forms import EmailForm, FileForm
from Mail_blacklist.models import Email
import csv
from _io import TextIOWrapper
from django.db.utils import IntegrityError


@login_required
def addEmail(request):
    if request.method=='POST':
        form=EmailForm(request.POST,
                       instance = Email())
        if form.is_valid():
            try:
                email = form.save(commit=False)
                email.user_id = request.user.id
                email.save()
                message="Email ajouté à la liste."
            except IntegrityError:
                message="Vous avez déjà ajouté cet email."
        
    form = EmailForm(instance=Email())
    return render(request,'Mail_blacklist/Adding_mail.html', locals())

@login_required
def addListEmail(request):
    if request.method=='POST':
        form=FileForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            redundant = 0
            success = 0
            f = request.FILES[list(request.FILES.keys())[0]]
            #request.Files are binary files but csv needs text file
            #TextIOWrapper makes f.file a text file
            f = TextIOWrapper(f.file,encoding=request.encoding)
            csv_read = csv.reader(f,delimiter=',')
            for line in csv_read:
                [mail, type_mail]=line
                email = Email(email=mail, user_id=request.user.id)
                email.type = type_mail
                try:
                    email.save()
                    success+=1
                except IntegrityError:
                    if Email.objects.filter(email=mail, 
                                            user_id=request.user.id):
                        redundant+=1
            done=True
    form = FileForm()
    return render(request, 'Mail_blacklist/Adding_mail_list.html', locals())

@login_required
def home(request):
    emails = Email.objects.filter(user_id=request.user.id)
    return render(request, 'Mail_blacklist/Home.html', locals())
