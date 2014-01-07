from django.http import HttpResponse

# Create your views here.
def index(request):
    f = open('surveys/staticpages/index.html','r')
    return HttpResponse(f.read())

def survey(request):
    f = open('surveys/staticpages/survey.html','r')
    return HttpResponse(f.read())

def privacy(request):
    f = open('surveys/staticpages/privacy.html','r')
    return HttpResponse(f.read())

def terms(request):
    f = open('surveys/staticpages/terms.html','r')
    return HttpResponse(f.read())

def contact(request):
    f = open('surveys/staticpages/contact.html','r')
    return HttpResponse(f.read())
