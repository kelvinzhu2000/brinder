from django.http import HttpResponse

import BrinderMail

def sendToRecipients(request):
    """
    if request.method == "POST":
        message_body = request.POST['message']
        names = request.POST['name_list']
        emails = request.POST['email_list']

        senderName = request.POST['sender_name'] #for test
        senderEmail = request.POST['sender_email']

        newMail = BrinderMail(names, emails, senderName, senderEmail, message_body)
        return HttpResponse(newMail.sendHelpRequest())
    """
