from odoo.tests.common import TransactionCase

class TestFleet(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestFleet, self).setUp(*args, **kwargs)
        self.odometer = self.env['fleet.vehicle.odometer']
        self.vehicle_model = self.env['fleet.vehicle']


    def test_vehicle_tag(self):
        """Test that a new vehicle company and model"""
        vehicle_data = {'model_id': 2, 'license_plate': 'ABCD123'}
        new_vehicle = self.vehicle_model.create(vehicle_data)
        
        odometer_value = {'value' : 10.34 , 'date': '2023-02-11', 'vehicle_id' :new_vehicle.id  }
        odoDetails = self.odometer.create(odometer_value)
        self.assertEqual(odoDetails.name, new_vehicle.name+' / ' + str(odoDetails.date))
        self.assertEqual(odoDetails.value, 10.34)
        self.assertEqual(odoDetails.vehicle_id.model_id.id, 2)
        WARNING = '\033[93m'
        ENDC = '\033[0m'
        print(f"{WARNING}4. ### Test case passed{ENDC}")