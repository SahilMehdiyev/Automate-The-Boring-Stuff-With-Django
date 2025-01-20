from django.apps import apps
from django.core.mail import EmailMessage
from django.conf import settings

def get_all_custom_models(): # try to get all the apps
    default_models = ['ContentType','Session','LogEntry','Group','Permission','Upload']
    custom_models = []
    for model in apps.get_models():
        # print(model.__name__)
        if model.__name__ not in default_models:
            custom_models.append(model.__name__)
            
    return custom_models


def send_email_notification(mail_subject,message,to_email):
    try:
        from_email = settings.DEFAULT_FROM_EMAIL
        mail = EmailMessage(mail_subject,message,from_email, to=[to_email])
        mail.send()
    except Exception as e:
        return e
    
    