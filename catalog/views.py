import os

from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    if request.method == 'POST':
        handle_uploaded_file(request.POST['name'], request.FILES['aud'])
    return render(request, 'index.html')


def handle_uploaded_file(filename, userfile):
    newFile = './audioInputFiles/'+filename+'.mp3'
    file = open(newFile, 'wb+')
    for chunk in userfile.chunks():
        file.write(chunk)
