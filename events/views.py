from django.shortcuts import render
from django.http import HttpResponse

from .models import Event 

def index(request):
	return render(request, 'events/index.html')


def event_listing(request):
	events = Event.objects.all()
	return render(request, 'events/event_listing.html', {'events': events}) 

def event_detail(request, name):
	data = {'Chill': '<h2>Chill on the beach for just $400</h2>',
			'Camping': '<h2>Camp with us for $40</h2>',
			'Flying': '<h2>Fly for free</h2>'}

	selection = data.get(name)

	if selection:
		return HttpResponse(selection)
	else:
		return HttpResponse('No such event in offering for now')