import random
import string
from django.http import HttpResponse
from django.contrib.auth.models import User
from surveys.models import survey, Message

from BrinderMail import BrinderMail

def randomStr(size=7, charSet=string.ascii_uppercase + string.digits):
    return ''.join([random.choice(charSet) for c in xrange(size)])


def sendToRecipients(request):
    
    if request.method == "POST":
        
        message_body = request.POST['message']
        randomUrl = randomStr()
        rootUrl = 'http://www.kelvinzhu.com/surveys'
        
        message_body = message_body + "<p>Link: <a href='{0}'>{1}</a></p>".format(rootUrl + '/' + randomUrl, rootUrl)
        
        names = request.POST.getlist('name_list[]')
        emails = request.POST.getlist('email_list[]')
        senderName = request.POST['sender_name'] #for test
        senderEmail = request.POST['sender_email']
        subject = "My wedding help request!"

        newMail = BrinderMail(names, emails, senderName, senderEmail, subject, message_body)
        newMail.send()
        
        #insert new message into database
        new_sender = User.objects.get(username=senderName)
        for name, email_addr in zip(names, emails):
            cur_survey = Survey.objects.all()[0]
            msg = Message(sender=new_sender, recipient_email=email_addr, survey=cur_survey, status="default", url=randomUrl)
            msg.save()
        
        return HttpResponse()

        

    
