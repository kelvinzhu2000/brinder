from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the surveys index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response  = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def privacy(request):
    f = open('surveys/staticpages/privacy.html','r')
    return HttpResponse(f.read())

def terms(request):
    f = open('surveys/staticpages/terms.html','r')
    return HttpResponse(f.read())

def contact(request):
    f = open('surveys/staticpages/contact.html','r')
    return HttpResponse(f.read())
