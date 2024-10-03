from django.core.management.base import BaseCommand
from dataentry.models import Student

class Command(BaseCommand):
    help = 'It will insert data to the database'
    
    def handle(self,*args, **kwargs):
        
        dataset = [
            {'roll_no': 1002, 'name': 'Test2', 'age': '22'},
            {'roll_no': 1003, 'name': 'Test3', 'age': '23'},
            {'roll_no': 1004, 'name': 'Test4', 'age': '24'},
        ]
        
        for data in dataset:
            # print(data['name'])
            Student.objects.create(roll_no=data['roll_no'], name= data['name'], age=data['age'])
        self.stdout.write(self.style.SUCCESS('Data inserted successfully!'))