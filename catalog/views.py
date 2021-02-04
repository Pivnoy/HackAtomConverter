from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponseRedirect


# Create your views here.

def index(request):
    if request.method == 'POST':
        handle_uploaded_file(request.POST['name'], request.FILES['aud'])
    return render(request, 'index.html')


def handle_uploaded_file(filename, userfile):
    filename += '.mp3'
    file = open(filename, 'wb+')
    for chunk in userfile.chunks():
        file.write(chunk)
