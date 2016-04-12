from django.shortcuts import render
from django.http import HttpResponse
from models import Illness, Testimonial
from django.core import serializers


def illness(request):
	return render(request,"portal/illness.html")

def testimonials(request):
	return render(request,"portal/testimonials.html")

def philosophy(request):
	return render(request, "portal/philosophy.html")

def about(request):
	return render(request, "portal/about.html")

def faq(request):
	return render(request, "portal/faq.html")

def get_illness(request, letter=None):
	illness_list = Illness.objects.filter(name__startswith=letter)
	return HttpResponse(serializers.serialize('json', illness_list))

def get_testimonial(request, id=None):
	return HttpResponse(id)


