from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import Http404
from .models import Event, Shift
from .forms import ShiftForm

# Create your views here.
def index(request):
    all_events = Event.objects.filter(published=True)
    paginator = Paginator(all_events, 5)
    page = request.GET.get('page')
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)

    context = {
        "latestevent": all_events.first(),
        "events": events,
    }
    return render(request, "events.html", context)

def event(request, id=None):
    if request.user.is_authenticated():
        userprofile = request.user
    else:
        userprofile = None
    try:
        events = Event.objects.filter(published=True)[:5]
    except IndexError:
        events = None
    event = get_object_or_404(Event, ~Q(published=False), id=id)
    event_shifts = Shift.objects.filter(event=event.id)
    context = {
        "userprofile": userprofile,
        "latestevents": events[:5],
        "event": event,
        "event_shifts": event_shifts,
    }
    return render(request, "eventpost.html", context)

def shift(request, id=None):
    if request.user.is_authenticated():
        userprofile = request.user
    else:
        userprofile = None
    shift = get_object_or_404(Shift, id=id)
    if shift.event.published == True:
        if request.method == 'POST':
            form = ShiftForm(request.POST)
            if form.is_valid():
                if shift.user != userprofile:
                    Shift.objects.filter(id=id).update(user=request.user)
                    return event(request, id=shift.event.id)
                else:
                    Shift.objects.filter(id=id).update(user=None)
                    return event(request, id=shift.event.id)
        else:
            form = ShiftForm()
        shift = get_object_or_404(Shift, id=id)
        context = {
            "userprofile": userprofile,
            "shift": shift,
            "form": form,
        }
        return render(request, "shift.html", context)
    else:
        raise Http404

def profile(request, user=None):
    if request.user.is_authenticated():
        userprofile = request.user
        shifts = Shift.objects.filter(user=userprofile).reverse()
    else:
        userprofile = None
        shifts = None
    context = {
        "userprofile": userprofile,
        "shifts": shifts,
    }
    return render(request, "profile.html", context)