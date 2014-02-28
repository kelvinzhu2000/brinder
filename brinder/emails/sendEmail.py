from django.http import HttpResponse

import BrinderMail

def sendToRecipients(request):
    if request.method == "POST":
        message_body = request.POST['message']
        names = request.POST['name_list']
        emails = request.POST['email_list']

        senderName = "chaoyan" #for test
        senderEmail = "aceyan8996@gmail.com"

        newMail = BrinderMail(names, emails, senderName, senderEmail, message_body)
        return HttpResponse(newMail.sendHelpRequest())
