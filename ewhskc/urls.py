"""ewhskc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.generic import RedirectView
import events.views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^android-chrome-192x192.png', RedirectView.as_view(url='/static/favicon/android-chrome-192x192.png', permanent=True)),
    url(r'^android-chrome-384x384.png', RedirectView.as_view(url='/static/favicon/android-chrome-384x384.png', permanent=True)),
    url(r'^apple-touch-icon.png', RedirectView.as_view(url='/static/favicon/apple-touch-icon.png', permanent=True)),
    url(r'^browserconfig.xml', RedirectView.as_view(url='/static/favicon/browserconfig.xml', permanent=True)),
    url(r'^favicon.ico', RedirectView.as_view(url='static/favicon/favicon.ico', permanent=True)),
    url(r'^favicon-16x16.png', RedirectView.as_view(url='/static/favicon/favicon-16x16.png', permanent=True)),
    url(r'^favicon-32x32.png', RedirectView.as_view(url='/static/favicon/favicon-32x32.png', permanent=True)),
    url(r'^manifest.json', RedirectView.as_view(url='/static/favicon/manifest.json', permanent=True)),
    url(r'^mstile-150x150.png', RedirectView.as_view(url='/static/favicon/mstile-150x150.png', permanent=True)),
    url(r'^safari-pinned-tab.svg', RedirectView.as_view(url='/static/favicon/safari-pinned-tab.svg', permanent=True)),
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('account.urls')),
    url(r'^profile/', events.views.profile, name="profile"),
    url(r'^updates/', include('updates.urls')),
    url(r'^events/', include('events.urls')),
]

handler404 = events.views.handler404
handler500 = events.views.handler500