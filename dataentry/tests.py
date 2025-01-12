from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.messages import get_messages
from unittest.mock import patch
from uploads.models import Upload  
import os




class ImportDataTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('import_data')
        
        self.test_csv = SimpleUploadedFile(
            'student_data.csv', b'roll_no,name,age\n1001,John,21\n1002,Jane,22',
            content_type='text/csv'
        )
        
        @patch('dataentry.views.call_command') 
        def test_import_data_success(self,mock_call_command):
            # POST
            response = self.client.post(self.url, {
                'model_name': 'Student', 
                'file_path': self.test_csv 
            })
            
            self.assertEqual(Upload.objects.count(),1)
            upload_instance = Upload.objects.first()
            self.assertEqual(upload_instance.model_name,'Student')
            self.assertTrue(os.path.exists(upload_instance.file_path)) # We check if the file exists
            
            mock_call_command.assert_called_once_with('importdata',upload_instance.file.path), 'Student'
            
            
            messages = list(get_messages(response.wsgi_request))
            self.assertEqual(len(messages),1)
            self.assertEqual(str(messages[0]),'Data imported successfuly')
            
            

        @patch('yourapp.views.call_command') 
        def test_import_data_failure(self, mock_call_command):
            mock_call_command.side_effect = Exception('Something went wrong')
            response = self.client.post(self.url, {
                'model_name': 'Student', 
                'file_path': self.test_csv 
            })
            self.assertEqual(Upload.objects.count(), 1)

            messages = list(get_messages(response.wsgi_request))
            self.assertEqual(len(messages), 1)
            self.assertEqual(str(messages[0]), 'Something went wrong')            