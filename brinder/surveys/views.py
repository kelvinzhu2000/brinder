from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required

from surveys.models import Message, Survey, Question
from surveys.forms import SurveyForm

@login_required
def index(request):
    f = open('surveys/staticpages/index.html','r')
    return HttpResponse(f.read())

@login_required
def survey(request, message_url):
    message = Message.objects.get(url=message_url)
    questions = message.survey.question_set.all()
    if request.method == 'POST':
        forms = SurveyForm(request.POST, questions=questions)
    else:
        form = SurveyForm(questions=questions)
    template = loader.get_template('surveys/survey.html')
    context = RequestContext(request, {
        'message': message,
        'questions': questions,
        'form': form,
    })
    return HttpResponse(template.render(context))

def privacy(request):
    f = open('surveys/staticpages/privacy.html','r')
    return HttpResponse(f.read())

def terms(request):
    f = open('surveys/staticpages/terms.html','r')
    return HttpResponse(f.read())

def contact(request):
    f = open('surveys/staticpages/contact.html','r')
    return HttpResponse(f.read())
