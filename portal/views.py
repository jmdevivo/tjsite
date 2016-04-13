from django.shortcuts import render
from django.http import HttpResponse
from models import Illness, Testimonial, FAQ, SiteText
from django.core import serializers
import json


def illness(request):
	return render(request,"portal/illness.html")

def testimonials(request):
	return render(request,"portal/testimonials.html")

def philosophy(request):
	siteObject = SiteText.objects.all().first()
	context = {
		"main_text" : siteObject.about_main
	}
	return render(request, "portal/philosophy.html")

def about(request):
	siteObject = SiteText.objects.all().first()
	context = {
		"main_text" : siteObject.about_main
	}
	return render(request, "portal/about.html", context)

def faq(request):
	context = {
		"faqs" : FAQ.objects.all()
	}
	return render(request, "portal/faq.html", context)

def get_illness(request, letter=None):
	illness_list = Illness.objects.filter(name__startswith=letter)
	return HttpResponse(serializers.serialize('json', illness_list))

def get_testimonial(request, id=None):
	response_data = {}
	response_data["id"] = id
	ls = [response_data]
	return HttpResponse(json.dumps(ls))


