from odoo.tests.common import TransactionCase
import datetime

class TestHospital(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestHospital, self).setUp(*args, **kwargs)
        self.doctor = self.env['hospital.doctor']
       


    def test_create_doctor(self):
        """Test that a new vehicle company and model"""
        doctor_details = { 
            'doctor_name' : 'team 2 doctor',  
            'age': 50,  
            'gender': 'female',
            'note': 'great doctor'
        }
        doc_details = self.doctor.create(doctor_details)
        self.assertEqual( doc_details.doctor_name , 'team 2 doctor')
        self.assertEqual( doc_details.age, 50)
        self.assertEqual( doc_details.note, 'great doctor')

        WARNING = '\033[93m'
        ENDC = '\033[0m'
        print(f"{WARNING}2. ### Test case passed{ENDC}")