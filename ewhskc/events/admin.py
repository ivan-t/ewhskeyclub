from django.contrib import admin
from .models import Event, Shift

# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_date', 'start_time', 'end_time', 'published', 'last_edited')
    list_filter = ('event_date',)
    list_editable = ('published',)
    ordering = ('-event_date', 'start_time', '-last_edited', 'published')
@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ('event', 'time', 'user')
    list_filter = ('event', 'user')
    list_editable = ('user',)
    ordering = ('-event', 'time')