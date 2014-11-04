from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.db import IntegrityError, DataError
from Site_App.models import Project

def index(request):
    return render(request, 'index.html')
	
def login(request):
	if request.user.is_authenticated():
		return render(request, 'login.html', {'message': "Logged in as "})
	else:
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
		return HttpResponseRedirect(reverse('index'))
	
def profile(request):
	a = Project.objects.filter(username=request.user.username)
	return render(request, 'profile.html', {'projects':a})
	
def project_edit(request):
    return render(request, 'project_edit.html')
	
def project_submit(request):
	username = request.user.username
	title = request.POST.get('title', 'empty')
	zipcode = request.POST.get('zipcode', 'empty')
	description = request.POST.get('descr', 'empty')
	try:
		project = Project(username=username, title=title, zipcode=zipcode, description=description)
		project.save()
	except(IntegrityError):
		return render(request, 'project_edit.html', {
            'error_message': "Error!"})
	else:
		return HttpResponseRedirect(reverse('index'))
	
def search(request):
	a = Project.objects.all()
	return render(request, 'search.html', {'projects':a})
