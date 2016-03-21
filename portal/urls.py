from django.conf.urls import patterns,url

from portal import views

urlpatterns = [
	url(r'^illness', views.illness),
	url(r'^testimonials', views.testimonials),
]