from django.contrib import messages
from django.conf import settings
from django.shortcuts import render,redirect

from .utils import get_all_custom_models
from uploads.models import Upload

from .tasks import import_data_task

def import_data(request):
    if request.method == 'POST':
        file_path = request.FILES.get('file_path')
        model_name = request.POST.get('model_name')
        
        # store this file inside the Upload model
        upload = Upload.objects.create(file = file_path, model_name=model_name)
        
        relative_path = str(upload.file.url)
        base_url = str(settings.BASE_DIR)
        
        file_path = base_url + relative_path
        
        #handle the import data task here 
        import_data_task(file_path,model_name)       
                    
        # triger the importdata command

        # show the message to the user
        messages.success(request, 'Your data is being imported, you will be notified once it is done. ')
        return redirect('import_data')
        
    else:
        custom_models = get_all_custom_models()
        context = {
            'custom_models': custom_models
        }
    return render(request, 'dataentry/importdata.html',context)