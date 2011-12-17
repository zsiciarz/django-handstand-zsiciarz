from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(
		regex=r'^login/$',
		view='django.contrib.auth.views.login',
		name='users-login',
		kwargs={
			'template_name': 'users/login.html',
	}),
	url(
		regex=r'^logout/$',
		view='django.contrib.auth.views.logout',
		name='users-logout',
		kwargs={
			'next_page': '/',
	}),
)
