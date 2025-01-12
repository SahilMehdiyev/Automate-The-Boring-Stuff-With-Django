from django.core.management.base import BaseCommand
import csv
# from dataentry.models import Student
from django.apps import apps
import datetime

# propsed command -> make exportdata


class Command(BaseCommand):
    help = 'Export data from the database to o CSV file'
    
    def add_arguments(self,parser):
        parser.add_argument('model_name',type=str, help='Model name')
    
    def handle(self,*args,**kwargs):
        model_name = kwargs['model_name'].capitalize()
        
        model = None
        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label, model_name)
                break
            except LookupError:
                pass
        if not model:
            self.stderr.write(f'Model {model_name} count not found')
            return 
        
        
        # fetch the data from the database 
        data = model.objects.all()

        # genearte the timestamo of current date and time
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')


        # define the csv file name/path
        file_path = f'exported_{model_name}_data_{timestamp}.csv'       
        
        # open the csv file and write the data
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            
            # write the csv header
            writer.writerow([field.name for field in model._meta.fields])
            
            # write data rows
            for dt in data:
                writer.writerow([getattr(dt,field.name) for field in model._meta.fields])
        
        self.stdout.write(self.style.SUCCESS('Data exported successfully!'))
        
        
                