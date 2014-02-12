import smtplib
import random
import string
#import surveys.models import Message

class BrinderMail:
    """
        A simple email conponent. Initialize as 
            new_emails = BrinderMail(receiverEmails, receiverNames, senderName, senderEmail)
        When sending wedding help request to receivers, use sendHelpRequest()
        After receivers submit surveys, sending thank you email to receivers, or sending notifications to
        senders, use sendAfterSurveyComplete() 
    """
    __smtpHost = 'smtp.gmail.com:587' #SMTP server default to be gmail
    __companyEmail = '' #company email address
    __companyDomain = 'brinder.com' #domain of the company
    __username = '' #account name of company email
    __password = '' #input the password of company email
    __subject = 'My wedding help request' #subject of the email
    
    #header template for email
    __header = 'From: {0} <{1}>\nTo: {2} <{3}>\nMIME-Version: 1.0\nContent-type: text/html\nSubject: {4}\n\n'
    #content template for email
    __message = '<p>Hi {0},</p><p>{1}</p><p>Thanks,</p><p>{2}</p>'
    

    def __init__(self, receiverEmails, receiverNames, senderName, senderEmail, message):
        try:
            self.senderName = senderName
            self.senderEmail = senderEmail
            self.receivers = zip(receiverEmails, receiverNames)
            self.messageContent = message
            self.smtpObj = smtplib.SMTP(BrinderMail.__smtpHost)
            self.smtpObj.starttls()
            self.smtpObj.login(BrinderMail.__username, BrinderMail.__password)
            print "log in"
        except smtplib.SMTPException as e:
            print "something wrong when log in"

    def randomStr(self, size=7, charset=string.ascii_uppercase + string.digits):
        return ''.join([random.choice(charset) for c in xrange(size)])


    def composeRequestMail(self, toName, toEmail):
        #create an email header
        header = BrinderMail.__header.format(BrinderMail.__companyDomain, BrinderMail.__companyEmail, toName, toEmail, BrinderMail.__subject)
        
        #generate random string for the survey url
        randomUrl = self.randomStr()
        #insert the new message to the database
        #newMessage = Message(self.senderEmail, toEmail, )
        
        rootUrl = 'http://www.kelvinzhu.com/surveys'
        
        content = self.messageContent + "<p>Link: <a href='{0}'>{1}</a></p>".format(rootUrl + '/' + randomUrl, rootUrl)
        
        #create main content for the email
        message = BrinderMail.__message.format(toName, content, self.senderName)
        
        return header + message

    def sendHelpRequest(self):
        try:    
            for i, receiver in enumerate(self.receivers):
                content = self.composeRequestMail(receiver[0], receiver[1])
                #print content
                self.smtpObj.sendmail(BrinderMail.__companyEmail, receiver[1], content)
        #print "successfully send to receiver {0}".format(receiver[1])
            self.smtpObj.quit()
            return "successfully send to your friends"
        except smtplib.SMTPException as e:
            self.smtpObj.quit()
            return "someting wrong with email sending"

    def sendAfterSurveyComplete(self):
        try:
            receiverName = self.receivers[0][0]
            receiverEmail = self.receivers[0][1]

            thankMessage = "Thank you for your patience. Your answers will be highly valuable for my wedding!"
            thankContent = self.compose(receiverName, receiverEmail, self.senderName, "Thank you for your help!", thankMessage)
            self.smtpObj.sendmail(BrinderMail.__companyEmail, receiverEmail, thankContent)
            print "send thank you email successfully to {0}".format(receiverEmail)
            noteMessage = "Your friend {0} has replied to your questions, please click the following link to see the detail!".format(receiverName)
            noteContent = self.compose(self.senderName, self.senderEmail, "Brinder Team", "{0} answers to your wedding questions".format(receiverName), noteMessage)
            self.smtpObj.sendmail(BrinderMail.__companyEmail, self.senderEmail, noteContent)
            print "send notification successfully to {0}".format(self.senderEmail)
            self.smtpObj.quit()
        except smtplib.SMTPException as e:
            self.smtpObj.quit()
            print "something wrong with sending "

#for test, also sample usage
if __name__ == '__main__':
    newMail = BrinderMail(['ace', 'chao'], ['yan1237319@126.com', 'chaoyanla@gmail.com'], 'Chao Yan', 'hypersaltla@hotmail.com', 'hahahaha')
    newMail.sendHelpRequest()
# newMail.sendAfterSurveyComplete()
