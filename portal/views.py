from django.shortcuts import render
from django.http import HttpResponse


def illness(request):
	return render(request,"portal/illness.html")

def testimonials(request):
	return render(request,"portal/testimonials.html")


