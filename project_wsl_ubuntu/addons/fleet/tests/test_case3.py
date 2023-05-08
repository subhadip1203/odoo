from odoo.tests.common import TransactionCase

class TestFleet(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestFleet, self).setUp(*args, **kwargs)
        self.vehicle_model = self.env['fleet.vehicle.model']
        self.car_brand = self.env['fleet.vehicle.model.brand']


    def test_vehicle_model_creation(self):
        """Test that a new vehicle company and model"""
        brand_data = {'name': 'XYZ'}
        toyotaBrand = self.car_brand.create(brand_data)
        model_data = {'brand_id': toyotaBrand.id,'name': 'camry', 'model_year': '2020'}
        new_vehicle_model = self.vehicle_model.create(model_data)
        self.assertEqual(new_vehicle_model.brand_id.id, toyotaBrand.id)
        self.assertEqual(new_vehicle_model.name, 'camry')
        WARNING = '\033[93m'
        ENDC = '\033[0m'
        print(f"{WARNING}3. ### Test case passed{ENDC}")