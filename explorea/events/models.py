from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    FUN = 'FN'
    RELAX = 'RX'
    EXP = 'EX'
    SIGHTS = 'SI'

    CATEGORY_CHOICES= (
        (FUN, 'fun'),
        (RELAX, 'relax'),
        (EXP, 'experience'),
        (SIGHTS, 'sights')
        )
    
    name = models.CharField(max_length=200)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)
    location = models.CharField(max_length=500)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default=FUN)

    def __str__(self):
    	return self.name

class EventRun(models.Model):

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date = models.DateField(blank=False, null=False)
    time = models.TimeField(blank=False, null=False)
    seats_available = models.PositiveIntegerField(blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)

    def __str__(self):
        return str(self.event) + str(self.date)