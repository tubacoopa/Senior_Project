from django.conf.urls import patterns, url

from Site_App import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^login/$', views.login, name='login'),
	url(r'^login_submit/$', views.login_submit, name='login_submit'),
	url(r'^site_logout/$', views.site_logout, name='site_logout'),
	url(r'^register/$', views.register, name='register'),
	url(r'^register_submit/$', views.register_submit, name='register_submit'),
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^project_edit/$', views.project_edit, name='project_edit'),
	url(r'^project_submit/$', views.project_submit, name='project_submit'),
	url(r'^search/$', views.search, name='search')
)