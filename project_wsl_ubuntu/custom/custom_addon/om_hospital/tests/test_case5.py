
from odoo.tests.common import TransactionCase
import datetime

class TestHospital(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestHospital, self).setUp(*args, **kwargs)
        self.patient = self.env['hospital.patient']
        self.doctor = self.env['hospital.doctor']
        self.appointment = self.env['hospital.appointment']
        
       


    def test_create_appointment(self):
        """Test that a new vehicle company and model"""

        patient_details = { 
            'name' : 'team 2',  
            'age': 25,  
            'gender': 'male',
            'note': 'some note'
        }
        p_details = self.patient.create(patient_details)

        doctor_details = { 
            'doctor_name' : 'team 2 doctor',  
            'age': 50,  
            'gender': 'female',
            'note': 'great doctor'
        }
        doc_details = self.doctor.create(doctor_details)

        appointment_deatils = {
            'name' : 'OT00020',
            'patient_id' : p_details.id,
            'doctor_id': doc_details.id,
            'note' : 'some note',
            'date_appointment' : '2022-05-10',
            'date_checkup': '2023-05-25 19:30:00'
        }
        apppoint_details = self.appointment.create(appointment_deatils)
        self.assertEqual( apppoint_details.patient_id.id , p_details.id)
        self.assertEqual( apppoint_details.doctor_id.id , doc_details.id)
        self.assertEqual( apppoint_details.note, 'some note')

        with self.assertRaises(AttributeError) as ctx:
            apppoint_details.note = "something else"
            apppoint_details.save()

        WARNING = '\033[93m'
        ENDC = '\033[0m'
        print(f"{WARNING}5. ### Test case passed{ENDC}")