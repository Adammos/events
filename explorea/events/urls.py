from django.urls import path

from . import views

app_name = 'events'

urlpatterns = [
	path('', views.index, name='index'),
	path('all/', views.event_listing, name='events'),
	path('detail/<int:pk>/', views.event_detail, name='detail'),
	path('eventruns/', views.eventRun_listing, name='eventruns'),
	path('mine/', views.myevents_listing, name='myevents'),
	path('new/', views.create_event, name='create_event'),
	path('update/<int:pk>/', views.update_event, name='update_event'),
	path('delete/<int:pk>/', views.delete_event, name='delete_event'),

	path('eventRun/new/', views.create_eventrun, name='create_eventrun'),
	path('updateRun/<int:pk>/', views.update_eventrun, name='update_eventrun'),
	path('deleteRun/<int:pk>/', views.remove_eventrun, name='remove_eventrun'),
	]