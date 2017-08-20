from django.db import models
from datetime import date
from django.contrib.auth.models import User


# Create your models here.
class Event(models.Model):
    title =  models.CharField(max_length=200)
    event_date = models.DateField(default=date.today)
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.TextField()
    last_edited = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_urls(self):
        return "/events/%s/" %(self.id)

    @property
    def is_past_due(self):
        return date.today() > self.event_date

    class Meta:
        ordering = ["-event_date", "start_time", "-last_edited"]

class Shift(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    time = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.event.title

    class Meta:
        ordering = ["-event", "time"]