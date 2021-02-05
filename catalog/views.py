import os

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from catalog.forms import SignUpForm

def index(request):
    if request.method == 'POST':
        handle_uploaded_file(request.POST['name'], request.FILES['aud'])
    return render(request, 'index.html')


def handle_uploaded_file(filename, userfile):
    newFile = './audioInputFiles/'+filename+'.mp3'
    file = open(newFile, 'wb+')
    for chunk in userfile.chunks():
        file.write(chunk)

def signup(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.email = form.cleaned_data.get('email')
            user.profile.dir_path = './'+ form.cleaned_data.get('username')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request,'signup.html',{'form':form})
