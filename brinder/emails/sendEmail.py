import random
import string
from django.http import HttpResponse

import BrinderMail

def randomStr(self, size=7, charSet=string.ascii_uppercase + string.digits):
    return ''.join([random.choice(charSet) for c in xrange(size)])


def sendToRecipients(request):
    
    if request.method == "POST":
        
        message_body = request.POST['message']
        randomUrl = randomStr()
        rootUrl = 'http://www.kelvinzhu.com/surveys'
        
        message_body = message_body + "<p>Link: <a href='{0}'>{1}</a></p>".format(rootUrl + '/' + randomUrl, rootUrl)
        
        names = request.POST['name_list']
        emails = request.POST['email_list']
        senderName = request.POST['sender_name'] #for test
        senderEmail = request.POST['sender_email']
        subject = "My wedding help request!"

        newMail = BrinderMail(names, emails, senderName, senderEmail, subject, message_body)
        return HttpResponse(newMail.send())

#def sendAfterSurvey(request):


    