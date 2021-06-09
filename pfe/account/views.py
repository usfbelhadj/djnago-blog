from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

def register(request):
    if request.method == 'POST':
        first_name =  request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if username == '' or  email == '':
            messages.add_message(request, messages.WARNING, "Please fill all the options")
            return redirect('register')
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.add_message(request, messages.WARNING, "Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.add_message(request, messages.WARNING, "Email Used")
                return redirect('register')
            user = User.objects.create_user(first_name=first_name, username=username, email=email, password=password1, last_name=last_name)
            user.save()
            messages.add_message(request, messages.SUCCESS ,"Done Create a new user")
        else:
            messages.add_message(request, messages.WARNING,"Check the password")
            return redirect('register')
        return redirect('login')
    
    else :
        return render(request, 'register.html')

def login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == '' or password == '':
            messages.add_message(request, messages.WARNING, "Please fill all the options")
            return redirect('login')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('blog')
           
        else:
            messages.add_message(request, messages.INFO,"Check the Username or Password")
            return redirect('login')
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')