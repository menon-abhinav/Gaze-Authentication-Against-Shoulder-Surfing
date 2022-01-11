from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth

# Create your views here.
def register(request):
    if request.method == "GET":
        return render(request, 'register.html')

    if request.method == "POST":
        username = request.POST["username"]
        fname = request.POST["first_name"]
        lname = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmPassword = request.POST["confirm_password"]
        
        if password != confirmPassword:
            return render(request, 'register.html', {'message': "Password & Confirm Password are not same"})

        newUser = User.objects.create_user(username = username, password = password, first_name = fname,last_name = lname, email = email)
        newUser.save()

        return redirect('/login')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'message' : "Invalid Id or password"})
            
    return redirect('/login')

def changePassword(request):
    pass

def forgotPassword(request):
    pass