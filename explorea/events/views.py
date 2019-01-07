from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.generic import ListView

from .models import Event, EventRun , Album, Image
from .forms import EventForm, EventRunForm, EventFilterForm, MultipleFileForm

def index(request):
	return render(request, 'events/index.html')


def event_listing(request, category=None):

    event_runs = EventRun.objects.all().filter_by_category(category)
    filter_form =  EventFilterForm(request.GET or None)
    
    if request.GET and filter_form.is_valid():
        data = filter_form.cleaned_data
    else:
        data = {}
    
    event_runs = event_runs.filter_first_available(**data)

    paginator = Paginator(event_runs, 4)
    page = request.GET.get('page')
    event_runs = paginator.get_page(page)

    return render(request, 'events/event_listing.html', 
        {'event_runs': event_runs, 'filter_form': filter_form})


def event_search(request):
    query = request.GET.get('q')
    events = Event.objects.search(query)

    filter_form =  EventFilterForm()
    paginator = Paginator(events, 4)
    page = request.GET.get('page')
    events = paginator.get_page(page)

    return render(request, 'events/event_listing.html', 
        {'events': events, 'filter_form': filter_form})



'''
def eventRun_listing(request):
	eventRuns = EventRun.objects.all()
	return render(request, 'events/eventRun_listing.html', {'eventRuns' : eventRuns})
'''

def event_detail(request, slug):
    event = Event.objects.get(slug=slug)
    runs = event.active_runs()
    args = {'event': event, 'runs': runs}

    return render(request, 'events/event_detail.html', args)

@login_required
def myevents_listing(request):
	events = Event.objects.filter(host=request.user)
	return render(request, 'events/myevents_listing.html', {'events': events})

@login_required
def delete_event(request, slug):
	event = get_object_or_404(Event, slug=slug)
	event.delete()
	return HttpResponseRedirect(reverse('events:myevents'))

@login_required
def update_event(request, slug):
    event = Event.objects.get(slug=slug)
    event_form = EventForm(request.POST or None, request.FILES or None, instance=event)
    file_form = MultipleFileForm(files=request.FILES or None)

    if request.method == 'POST':
        if event_form.is_valid() and file_form.is_valid():
            event = event_form.save()

            for file in request.FILES.getlist('gallery'):
                Image.objects.create(album=event.album, image=file, title=file.name)

            return redirect(event.get_absolute_url())

    return render(request, 'events/create_event.html', 
        {'event_form': event_form, 'file_form': file_form, 'event': event})

@login_required
def create_event(request):
    event_form = EventForm(request.POST or None, request.FILES or None)
    file_form = MultipleFileForm(files=request.FILES or None)

    if request.method == 'POST':
 
        if event_form.is_valid() and file_form.is_valid():
            event = event_form.save(commit=False)
            event.host = request.user
            event.save()
            # save the individual images
            for file in request.FILES.getlist('gallery'):
                Image.objects.create(album=event.album, image=file, title=file.name)

            return redirect(event.get_absolute_url())

    return render(request, 'events/create_event.html', 
         {'event_form': event_form, 'file_form': file_form})

@login_required
def remove_eventrun(request, pk):
	eventrun = get_object_or_404(EventRun, pk=pk)
	eventrun.delete()
	return HttpResponseRedirect(reverse('events:eventRuns'))

@login_required
def update_eventrun(request, pk):
	eventrun = get_object_or_404(EventRun, pk=pk)
	if request.method == 'POST':
		form = EventRunForm(request.POST, instance=eventrun)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('events:eventRuns'))
	else:
		form = EventRunForm(instance=eventrun)
	return render(request, 'events/update_eventrun.html', {'form': form})

@login_required
def create_eventrun(request):
	if request.method == 'POST':
		form = EventRunForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('events:eventRuns'))
	else:
		form = EventRunForm()
	return render(request, 'events/create_eventrun.html', {'form': form})