from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from surveys.models import Message, Survey, Question, DropDownChoice, \
    DropDownAnswer, TrueFalseAnswer, OrderingChoiceRankings, OrderingAnswer, \
    ExplanationAnswer, RadioButtonChoice, RadioButtonAnswer, \
    MultipleChoiceChoice, MultipleChoiceAnswer
from surveys.forms import SurveyForm

@login_required
def index(request):
    f = open('surveys/staticpages/index.html','r')
    return HttpResponse(f.read())

@login_required
def survey(request, message_url):
    message = Message.objects.get(url=message_url)
    questions = message.survey.question_set.order_by('rank').all()
    if request.method == 'POST':
        form = SurveyForm(request.POST, questions=questions)
        if form.is_valid():
            for question in questions:
                data = form.cleaned_data['question_{index}'.format(index=question.id)]

                if hasattr(question, 'dropdownquestion'):
                    choice = DropDownChoice.objects.get(id=int(data))
                    try:
                        answer = DropDownAnswer.objects.get(message=message, question=question)
                    except DropDownAnswer.DoesNotExist:
                        answer = DropDownAnswer(message=message, question=question)
                    answer.value = choice
                    answer.save()
                elif hasattr(question, 'truefalsequestion'):
                    try:
                        answer = TrueFalseAnswer.objects.get(message=message, question=question)
                    except TrueFalseAnswer.DoesNotExist:
                        answer = TrueFalseAnswer(message=message, question=question)
                    answer.value = data
                    answer.save()
                elif hasattr(question, 'explanationquestion'):
                    try:
                        answer = ExplanationAnswer.objects.get(message=message, question=question)
                    except ExplanationAnswer.DoesNotExist:
                        answer = ExplanationAnswer(message=message, question=question)
                    answer.value = data
                    answer.save()
                elif hasattr(question, 'radiobuttonquestion'):
                    choice = RadioButtonChoice.objects.get(id=int(data))
                    try:
                        answer = RadioButtonAnswer.objects.get(message=message, question=question)
                    except RadioButtonAnswer.DoesNotExist:
                        answer = RadioButtonAnswer(message=message, question=question)
                    answer.value = choice
                    answer.save()
                elif hasattr(question, 'multiplechoicequestion'):
                    # Delete all the original answers
                    answers = MultipleChoiceAnswer.objects.filter(message=message, question=question)
                    for answer in answers:
                        answer.delete()

                    # Add in the new answers
                    for choice in data:
                        choice = MultipleChoiceChoice.objects.get(id=int(choice))
                        answer = MultipleChoiceAnswer(message=message, question=question, value=choice)
                        answer.save()
                elif hasattr(question, 'orderingquestion'):
                    # Get the answer to associate the ordering choices with
                    try:
                        answer = OrderingAnswer.objects.get(message=message, question=question)
                    except OrderingAnswer.DoesNotExist:
                        answer = OrderingAnswer(message=message, question=question)
                        answer.save()

                    raw_choices = question.orderingquestion.orderingchoice_set.order_by('id').all()
                    for key, value in enumerate(data):
                        try:
                            choice_ranking = OrderingChoiceRankings.objects.get(answer=answer, choice=raw_choices[key])
                        except OrderingChoiceRankings.DoesNotExist:
                            choice_ranking = OrderingChoiceRankings(answer=answer, choice=raw_choices[key])
                        choice_ranking.value = value
                        choice_ranking.save()
            return HttpResponseRedirect(reverse('thanks'))
    else:
        form = SurveyForm(questions=questions)
    template = loader.get_template('surveys/survey.html')
    context = RequestContext(request, {
        'message': message,
        'questions': questions,
        'form': form,
    })
    return HttpResponse(template.render(context))

def thanks(request):
    f = open('surveys/staticpages/thanks.html','r')
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
