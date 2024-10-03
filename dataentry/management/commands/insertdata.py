from django.core.management.base import BaseCommand
from dataentry.models import Student

class Command(BaseCommand):
    help = 'It will insert data to the database'
    
    def handle(self,*args, **kwargs):
        
        dataset = [
            {'roll_no': 1002, 'name': 'Test2', 'age': '24'},
            {'roll_no': 1003, 'name': 'Test3', 'age': '25'},
            {'roll_no': 1004, 'name': 'Test4', 'age': '26'},
        ]
        
        for data in dataset:
            roll_no = data['roll_no']
            existing_record = Student.objects.filter(roll_no=roll_no).exists()
            
            if not existing_record:
                Student.objects.create(roll_no=data['roll_no'], name= data['name'], age=data['age'])
                
            else:
                self.stdout.write(self.style.WARNING(f'Student with roll no {roll_no} already exists! '))
                    
        self.stdout.write(self.style.SUCCESS('Data inserted successfully!'))