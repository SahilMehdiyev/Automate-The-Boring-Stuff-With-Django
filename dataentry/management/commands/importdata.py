import csv
from django.core.management.base import BaseCommand
from dataentry.models import Student

class Command(BaseCommand):
    help = 'Import data from CVS file'
    
    
    def add_arguments(self,parser):
        parser.add_argument('file_path',type=str, help = 'Path to the CSV file')
    
    
    def handle(self,*args,**kwargs):
        
        file_path = kwargs['file_path']
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Student.objects.create(**row)
                
        self.stdout.write(self.style.SUCCESS('Data inserted succesfully'))
        
        
        