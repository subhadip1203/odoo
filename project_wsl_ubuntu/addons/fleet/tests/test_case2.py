from odoo.tests.common import TransactionCase

class TestFleet(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestFleet, self).setUp(*args, **kwargs)
        self.vehicle_model = self.env['fleet.vehicle']


    def test_vehicle_Numberplate_creation(self):
        """Test that a new vehicle can be created"""
        license_plateno = "ABCD123"
        vehicle_data = {'model_id': 2, 'license_plate': license_plateno}
        new_vehicle = self.vehicle_model.create(vehicle_data)
        self.assertEqual(new_vehicle.model_id.id, 2)
        self.assertEqual(new_vehicle.license_plate, license_plateno)
        WARNING = '\033[93m'
        ENDC = '\033[0m'
        print(f"{WARNING}FLEET 2. ### Test case passed{ENDC}")