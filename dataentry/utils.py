from django.apps import apps


def get_all_custom_models(): # try to get all the apps
    default_models = ['ContentType','Session','LogEntry','Group','Permission','Upload']
    custom_models = []
    for model in apps.get_models():
        # print(model.__name__)
        if model.__name__ not in default_models:
            custom_models.append(model.__name__)
            
    return custom_models