from odoo.exceptions import ValidationError
from odoo.tests.common import TransactionCase
import datetime

class TestHospital(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestHospital, self).setUp(*args, **kwargs)
        self.patient = self.env['hospital.patient']
        

    def test_duplicate_patient(self):
        """Test that a new vehicle company and model"""

        patient_details = { 
            'name' : 'team 2',  
            'age': 25,  
            'gender': 'male',
            'note': 'some note'
        }
        p_details = self.patient.create(patient_details)
        self.assertEqual( p_details.name , 'team 2')
        self.assertEqual(p_details.age, 25)
        self.assertEqual(p_details.note, 'some note')

        with self.assertRaises(ValidationError) as ctx:
            self.patient.create(patient_details)
           
        WARNING = '\033[93m'
        ENDC = '\033[0m'
        print(f"{WARNING}4. ### Test case passed{ENDC}")