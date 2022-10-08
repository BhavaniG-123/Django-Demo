import imp
from django.http import HttpResponse
from django.shortcuts import render

from DemoApp.models import User

def home(req):
    return render(req, 'index.html', {'id' : '', 'alert' : ''})

def login(req):
    return render(req, 'login.html', {})

def verify(req):
    print(req.POST)
    users = User.objects.filter(username = req.POST['username'], pwd = req.POST['password'])
    if len(users) > 0:
        return render(req, 'landing_page.html', {'id' : req.POST['username'], 'alert' : ''})

    else:
        return render(req, 'index.html', {'id' : '', 'alert' : 'Invalid username or password'})

def logout(req):
    return render(req, 'index.html', {'id' : '', 'alert' : 'Logged out successfully'})

def register(req):
    return render(req, 'register.html', {})

def register_data(req):
    data = req.POST
    User(
        username = data['username'], 
        pwd = data['password'], 
        name = data['name'], 
        contact_no = data['contact_no'], 
        gender = data['gender'], 
        address = data['address']
    ).save()

    return render(req, 'index.html', {'id' : '', 'alert' : 'User created successfully'})