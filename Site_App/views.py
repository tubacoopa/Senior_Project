from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')
	
def login(request):
    return render(request, 'login.html')
	
def register(request):
    return render(request, 'register.html')
	
def profile(request):
    return render(request, 'profile.html')
	
def search(request):
    return render(request, 'search.html')
