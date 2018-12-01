from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Event, EventRun 
from .forms import CreateEventForm, CreateEventRunForm

def index(request):
	return render(request, 'events/index.html')


def event_listing(request):
	events = Event.objects.all()
	return render(request, 'events/event_listing.html', {'events': events})

def eventRun_listing(request):
	eventRuns = EventRun.objects.all()
	return render(request, 'events/eventRun_listing.html', {'eventRuns' : eventRuns})

def event_detail(request, pk):
	try:
		event = Event.objects.get(pk=pk)
		runs = event.eventrun_set.all().order_by('-date')
	except Event.DoesNotExist:	
		return HttpResponse('Does not exist')
	return render(request, 'events/event_detail.html', {'event': event, 'runs': runs})

@login_required
def myevents_listing(request):
	events = Event.objects.filter(host=request.user)
	return render(request, 'events/myevents_listing.html', {'events': events})

@login_required
def delete_event(request, pk):
	event = get_object_or_404(Event, pk=pk)
	event.delete()
	return HttpResponseRedirect(reverse('events:myevents'))

@login_required
def update_event(request, pk):
	event = get_object_or_404(Event, pk=pk)
	if request.method == 'POST':
		form = CreateEventForm(request.POST, instance=event)
		if form.is_valid():
			updated_event = form.save(commit=False)
			updated_event.host = request.user
			updated_event.save()
			return HttpResponseRedirect(reverse('events:myevents'))
	else:
		form = CreateEventForm(instance=event)
	return render(request, 'events/update_event.html', {'form': form})

@login_required
def create_event(request):
	if request.method == 'POST':
		form = CreateEventForm(request.POST)
		if form.is_valid():
			new_event = form.save(commit=False)
			new_event.host = request.user
			new_event.save()
			return HttpResponseRedirect(reverse('events:myevents'))
	else:
		form = CreateEventForm()

	return render(request, 'events/create_event.html', {'form': form} )

@login_required
def remove_eventrun(request, pk):
	eventrun = get_object_or_404(EventRun, pk=pk)
	eventrun.delete()
	return HttpResponseRedirect(reverse('events:eventRuns'))

@login_required
def update_eventrun(request, pk):
	eventrun = get_object_or_404(EventRun, pk=pk)
	if request.method == 'POST':
		form = CreateEventRunForm(request.POST, instance=eventrun)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('events:eventRuns'))
	else:
		form = CreateEventRunForm(instance=eventrun)
	return render(request, 'events/update_eventrun.html', {'form': form})

@login_required
def create_eventrun(request):
	if request.method == 'POST':
		form = CreateEventRunForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('events:eventRuns'))
	else:
		form = CreateEventRunForm()
	return render(request, 'events/create_eventrun.html', {'form': form})