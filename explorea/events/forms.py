from django import forms

from .models import Event, EventRun
class CreateEventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = [
            'name',
            'description',
            'location',
            'category',
        ]

class CreateEventRunForm(forms.ModelForm):
    date = forms.DateField(input_formats=["%d.%m.%Y"], widget=forms.DateInput(format = '%d.%m.%Y'))

    class Meta:
        model = EventRun
        fields = [
          'event',
            'date',
            'time',
            'seats_available',
            'price',
        ]

