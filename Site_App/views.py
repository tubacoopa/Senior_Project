from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.db import IntegrityError, DataError
from Site_App.models import Profile

def index(request):
    return render(request, 'index.html')
	
def login(request):
    return render(request, 'login.html')
	
def register(request):
    return render(request, 'register.html')
	
def register_submit(request):
	username = request.POST.get('username', 'empty')
	password = request.POST.get('password', 'empty')
	email = request.POST.get('email', 'empty')
	try:
		user = User.objects.create_user(username, email, password)
		user.save()
	except(IntegrityError):
		return render(request, 'register.html', {
            'error_message': "Username taken!"})
	else:
		user = authenticate(username=username, password=password)
		auth_login(request, user)
		return HttpResponseRedirect(reverse('profile_edit'))
	
def profile(request):
    return render(request, 'profile.html')
	
def profile_edit(request):
    return render(request, 'profile_edit.html')
	
def profile_submit(request):
	username = request.user.username
	title = request.POST.get('title', 'empty')
	zipcode = request.POST.get('zipcode', 'empty')
	description = request.POST.get('descr', 'empty')
	try:
		profile = Profile(username=username, title=title, zipcode=zipcode, description=description)
		profile.save()
	except(IntegrityError):
		return render(request, 'profile_edit.html', {
            'error_message': "Error!"})
	else:
		return HttpResponseRedirect(reverse('index'))
	
def search(request):
    return render(request, 'search.html')
