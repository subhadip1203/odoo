from odoo.tests.common import TransactionCase
import datetime

class TestFleet(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestFleet, self).setUp(*args, **kwargs)
        self.vehicle_model = self.env['fleet.vehicle']
        self.vehicle_contract = self.env['fleet.vehicle.log.contract']


    def test_vehicle_contract(self):
        """Test that a new vehicle company and model"""
        vehicle_data = {'model_id': 2, 'license_plate': 'ABCD123'}
        new_vehicle = self.vehicle_model.create(vehicle_data)

        contractDeatils = { 
            'vehicle_id' :new_vehicle.id ,  
            'cost_frequency': 'monthly',  
            'expiration_date': '2023-08-07'
        }
        contractDeatils = self.vehicle_contract.create(contractDeatils)
        self.assertEqual( str(contractDeatils.expiration_date)[:10], '2023-08-07')
        self.assertEqual(contractDeatils.cost_frequency, 'monthly')
        self.assertEqual(contractDeatils.vehicle_id.model_id.id, 2)

        WARNING = '\033[93m'
        ENDC = '\033[0m'
        print(f"{WARNING}5. ### Test case passed{ENDC}")