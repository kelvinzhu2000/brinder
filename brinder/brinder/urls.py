from django.conf.urls import patterns, include, url

from surveys import views
from emails import sendEmail
from brinderregistration import register

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'brinder.views.home', name='home'),
    url(r'^$', views.index, name='index'),
    url(r'^surveys/', include('surveys.urls', namespace="surveys")),
    url(r'^privacy/', views.privacy, name='privacy'),
    url(r'^thanks/', views.thanks, name='thanks'),
    url(r'^terms/', views.terms, name='terms'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^sendEmail/', sendEmail.sendToRecipients, name='sendEmail'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/register/$', register.RegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls'))
)
