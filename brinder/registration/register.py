'''
Created on Feb 11, 2014

@author: Frederich
'''

from registration.backends.simple.views import RegistrationView as SimpleRegistrationView
from django.conf import settings
from django.core.urlresolvers import reverse

class RegistrationView(SimpleRegistrationView):
    def __init__(self):
        SimpleRegistrationView.__init__(self)
    def get_success_url(self, request, user):
        url = request.build_absolute_uri(reverse('index'))
        return url