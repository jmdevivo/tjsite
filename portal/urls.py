from django.conf.urls import patterns,url

from portal import views

urlpatterns = [
	url(r'^v1/illness/(?P<letter>\w{0,50})$', views.get_illness),
	url(r'^v1/testimonial/(?P<id>\w{0,50})$', views.get_testimonial),
	url(r'^illness', views.illness),
	url(r'^testimonials', views.testimonials),
	url(r'^philosophy', views.philosophy),
	url(r'^about', views.about),
	url(r'^faq', views.faq),
]