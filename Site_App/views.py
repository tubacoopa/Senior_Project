from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.db import IntegrityError, DataError
from django.db.models import Q
from Site_App.models import Project, Join

def index(request):
    return render(request, 'index.html')
	
def login(request):
	if request.user.is_authenticated():
		return render(request, 'login.html', {'message': "Logged in as "})
	else:
		return render(request, 'login.html')
		
def login_submit(request):
	username = request.POST.get('username', 'empty')
	password = request.POST.get('password', 'empty')
	user = authenticate(username=username, password=password)
	if user is not None:
		auth_login(request, user)
	if request.user.is_authenticated():
		return render(request, 'login.html', {'message': "Logged in as "})
	else:
		return render(request, 'login.html', {'message': "Invalid login!"})
	
def site_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))	
	
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
	joins = Join.objects.filter(username=request.user.username)
	a = Project.objects.filter(username=request.user.username)
	list = []
	for join in joins:
		list.append(join.title)
	b = Project.objects.filter(title__in=list)
	return render(request, 'profile.html', {'projects':a, 'joins':b})
	
def join(request, title):
	join = Join(username=request.user.username, title=title)
	join.save()
	return HttpResponseRedirect(reverse('index'))
	
def delete(request, title):
	project = Project.objects.get(title=title)
	project.delete()
	return HttpResponseRedirect(reverse('index'))
	
def edit(request, title):
	project = Project.objects.get(title=title)
	return render(request, 'edit.html', {'project':project})
	
def edit_submit(request, title):
	project = Project.objects.get(title=title)
	project.zipcode = zipcode = request.POST.get('zipcode', 'empty')
	project.description = request.POST.get('descr', 'empty')
	project.save()
	return HttpResponseRedirect(reverse('index'))
	
def project(request, title):
	project = Project.objects.get(title=title)
	return render(request, 'project.html', {'project':project})
	
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
	terms = request.POST.get('search', '')
	if (terms == ''):
		a = Project.objects.all()
		return render(request, 'search.html', {'projects':a})
	else:
		for term in terms.split(' '):
			a = Project.objects.filter(Q(title__icontains=term) | Q(description__icontains=term) | Q(username__icontains=term) | Q(zipcode__icontains=term))
			return render(request, 'search.html', {'projects':a})