from django.conf.urls import patterns, include, url

from surveys import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'brinder.views.home', name='home'),
    url(r'^surveys/', include('surveys.urls')),
    url(r'^privacy/', views.privacy, name='privacy'),
    url(r'^terms/', views.terms, name='terms'),
    url(r'^contact/', views.contact, name='contact'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
