from django.http import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        return HttpResponse("Converter Page")
    else:
        return redirect('/login')
