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
        x = {
            'username' : users[0].username,
            'name' : users[0].name, 
            'contact_no' : users[0].contact_no, 
            'gender' : users[0].gender, 
            'address' : users[0].address
        }
        return render(req, 'landing_page.html', x)

    else:
        return render(req, 'index.html', {'id' : '', 'alert' : 'Invalid Username or Password'})

def logout(req):
    return render(req, 'index.html', {'id' : '', 'alert' : 'Logged Out Successfully !'})

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

    return render(req, 'index.html', {'id' : '', 'alert' : 'User Created Successfully !'})