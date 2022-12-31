from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

def login(request):

    if request.method == 'POST':
        email = request.POST['email'].replace(' ','').lower() #check if email is entered after sumited form then store as lower and remove any space
        password = request.POST['password']

        user = auth.authenticate(username=email,password=password)
        if user:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials or User does not exist. Please verify your credentials or create and account!")
            return redirect('login')
    

    return render(request, 'authorisation/login.html')

def register(request):
    if request.method == 'POST':
        email = request.POST['email'].replace(' ','').lower() #check if email is entered after sumited form then store as lower and remove any space
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if not password1 == password2:
            messages.error(request, "Passwords do not Match")
            return redirect('register')
        
        if User.objects.filter(email = email).exists():
            messages.error(request, "A user with the same email address already exist, Please use a different email".format(email))
            return redirect('register')
        
        user = User.objects.create_user(email=email, username=email, password=password1) #used the email for username
        user.save()

        auth.login(request,user)
        return redirect('home')

        print('Usernae sumitted was {}'.format(email))
        return redirect('register')
    return render(request, 'authorisation/register.html')
