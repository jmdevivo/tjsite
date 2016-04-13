from django.shortcuts import render
from django.http import HttpResponse
from portal.models import SiteText

def index(request):
	siteObject = SiteText.objects.all().first()
	context = {
		"main_text": siteObject.home_body,
		"side_text" : siteObject.home_side
	}
	return render(request,"portal/index.html", context)