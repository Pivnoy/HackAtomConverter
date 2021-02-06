import os
import time

import psycopg2
import uuid
from django.core.files import File
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, FileResponse
from catalog.forms import SignUpForm


def index(request):
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['aud'])
        return render(request, 'Frontend/Download.html')
    return render(request, 'Frontend/Index.html')


def download_file(request):
    file = open('OutputFiles/pizda.txt', 'rb')
    myFile = File(file)
    response = HttpResponse(myFile, content_type='file')
    response['Content-Disposition'] = 'attachment; filename=input.txt'
    return response


def handle_uploaded_file(userfile):
    filename = str(uuid.uuid4())
    newFile = './audioInputFiles/' + filename + '.mp3'
    file = open(newFile, 'wb+')
    for chunk in userfile.chunks():
        file.write(chunk)
    dataBaseWorker(filename, newFile)


def dataBaseWorker(fileName, pathToFile):
    con = psycopg2.connect(
        database="anna",
        user="anna",
        password="",
        host="127.0.0.1",
        port="5432"
    )
    cursor = con.cursor()
    cursor.execute("INSERT INTO TAB (audio, path, proc) VALUES (%s, %s, %s)", (fileName, pathToFile, False))
    con.commit()
    # cursor.execute("SELECT FROM TAB WHERE audio=%s", fileName)
    # row = cursor.fetchall()


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.email = form.cleaned_data.get('email')
            user.profile.dir_path = './' + form.cleaned_data.get('username')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse("Invalid Login or password")
    else:
        return render(request, 'login.html', {})


def user_logout(request):
    logout(request)
    return redirect('/')


def download_file(request):
    con = psycopg2.connect(
        database="anna",
        user="anna",
        password="",
        host="127.0.0.1",
        port="5432"
    )
    cursor = con.cursor()
    cursor.execute("SELECT * from TEXT WHERE proc=TRUE")
    row = cursor.fetchall()
    fileName = 'OutputFiles/' + str(row[0][0]) + '.txt'
    file = open(fileName, 'rb')
    myFile = File(file)
    response = HttpResponse(myFile, content_type='file')
    response['Content-Disposition'] = 'attachment; filename=input.txt'
    return response


def read_text(request):
    con = psycopg2.connect(
        database="anna",
        user="anna",
        password="",
        host="127.0.0.1",
        port="5432"
    )
    cursor = con.cursor()
    cursor.execute("SELECT * from TEXT WHERE proc=TRUE")
    row = cursor.fetchall()
    fileName = 'OutputFiles/' + str(row[0][0]) + '.txt'
    file = open(fileName, 'r', encoding='utf-8')
    string = []
    for f in file:
        string.append(f)
    html = "<p>%s</p>" % string[0]
    return HttpResponse(html)
