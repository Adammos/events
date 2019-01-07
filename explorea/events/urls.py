from django.urls import path

from . import views

app_name = 'events'

urlpatterns = [
	path('', views.event_listing, name='events'),
	path('search/', views.event_search, name='search'),

	path('detail/<slug:slug>/', views.event_detail, name='detail'),
	path('update/<slug:slug>/', views.update_event, name='update_event'),
	path('delete/<slug:slug>/', views.delete_event, name='delete_event'),

	#path('eventruns/', views.eventRun_listing, name='eventruns'),
	path('mine/', views.myevents_listing, name='myevents'),
	path('new/', views.create_event, name='create_event'),


	path('eventRun/new/', views.create_eventrun, name='create_eventrun'),
	path('updateRun/<int:pk>/', views.update_eventrun, name='update_eventrun'),
	path('deleteRun/<int:pk>/', views.remove_eventrun, name='remove_eventrun'),

	path('<category>/', views.event_listing, name='events_by_category'),
	]