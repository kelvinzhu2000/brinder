import smtplib
#import surveys.models import Message

import yaml
import os

def get_conf(yaml_path):
    yfile = file(yaml_path, 'r')

    yconf = yaml.load(yfile)
    conf = {}

    if 'common' in yconf:
        common = yconf['common']

        # everything else should map 1-to-1
        conf.update(common)

    return conf

PROJECT_PATH = os.path.join(os.path.dirname(__file__), '../brinder')
CONF_PATH = 'conf.yaml'

ENV_CONF_PATH = os.path.join(PROJECT_PATH, CONF_PATH)

env_conf            = get_conf(ENV_CONF_PATH)
env_email_conf      = env_conf['email']

class BrinderMail:
    """
        A simple email wrapper that compose email content and perform sending. Initialize as 
            new_emails = BrinderMail(receiverEmails, receiverNames, senderName, senderEmail)
        Use setContent(subject, message) to reset subject and message content
        Use send() to send email
    """
    __smtpHost = env_email_conf['host'] #SMTP server default to be gmail
    __companyEmail = env_email_conf['email'] #company email address
    __companyDomain = env_email_conf['domain'] #domain of the company
    __username = env_email_conf['user'] #account name of company email
    __password = env_email_conf['password'] #input the password of company email
   
    #header template for email
    __header = 'From: {0} <{1}>\nTo: {2} <{3}>\nMIME-Version: 1.0\nContent-type: text/html\nSubject: {4}\n\n'
    #content template for email
    __message = '<p>Hi {0},</p><p>{1}</p><p>Thanks,</p><p>{2}</p>'
    

    def __init__(self, receiverEmails, receiverNames, senderName, senderEmail, subject='', message=''):
        try:
            self.senderName = senderName
            self.senderEmail = senderEmail
            self.receivers = zip(receiverEmails, receiverNames)
            self.messageContent = message
            self.subject = subject
            self.smtpObj = smtplib.SMTP(BrinderMail.__smtpHost)
            self.smtpObj.starttls()
            self.smtpObj.login(BrinderMail.__username, BrinderMail.__password)
            print "log in"
        except smtplib.SMTPException as e:
            print "something wrong when log in"

    def setContent(self, new_subject, new_message):
        self.subject = new_subject
        self.messageContent = new_message

    def compose(self, toName, toEmail):
        header = BrinderMail.__header.format(BrinderMail.__companyDomain, BrinderMail.__companyEmail, toName, toEmail, self.subject)
        message = BrinderMail.__message.format(toName, self.messageContent, self.senderName)
        return header + message

    def send(self):
        try:    
            for i, receiver in enumerate(self.receivers):
                content = self.compose(receiver[0], receiver[1])
                #print content
                self.smtpObj.sendmail(BrinderMail.__companyEmail, receiver[1], content)
        #print "successfully send to receiver {0}".format(receiver[1])
            self.smtpObj.quit()
            return "successfully send email"
        except smtplib.SMTPException as e:
            self.smtpObj.quit()
            return "someting wrong with email sending"

   #for test, also sample usage
if __name__ == '__main__':
    #message_body = "need your wedding help!"
    #size = 7
    #charSet = string.ascii_uppercase + string.digits
    #randomUrl = ''.join([random.choice(charSet) for c in xrange(size)])
    
    #rootUrl = 'http://www.kelvinzhu.com/surveys'
        
        #message_body = message_body + "<p>Link: <a href='{0}'>{1}</a></p>".format(rootUrl + '/' + randomUrl, rootUrl)

#newMail = BrinderMail(['ace', 'chao'], ['yan1237319@126.com', 'chaoyanla@gmail.com'], 'Chao Yan', 'hypersaltla@hotmail.com', 'wedding help', message_body)
    
    #newMail.send()
    
    message_body = "Thank you for your patience. Your answers will be highly valuable for my wedding!"
    newMail = BrinderMail(['ace'], ['yan1237319@126.com'], 'Chao Yan', 'hypersaltla@hotmail.com', 'Thank you for your help!', message_body)

    newMail.send()

    message_body = "Your friend <Chao Yan> has replied to your questions, please click the following link to see the detail!"
    newMail.setContent("Chao Yan answers to your wedding questions", message_body)
    #newMail = BrinderMail(['Chao Yan'], ['hypersaltla@hotmail.com'], 'brinder.com', 'brinder@gmail.com', "<Chao Yan> answers to your wedding questions", message_body)

    newMail.send()

# newMail.sendAfterSurveyComplete()
