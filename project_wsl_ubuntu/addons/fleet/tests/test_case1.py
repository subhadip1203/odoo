from odoo.tests.common import TransactionCase

class TestFleet(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestFleet, self).setUp(*args, **kwargs)
        self.vehicle_model = self.env['fleet.vehicle']
        self.res_partner_model = self.env['res.partner']

    def test_vehicle_creation(self):
        """Test that a new vehicle can be created"""
        partner_data = {'name': 'Subhadip'}
        new_partner = self.res_partner_model.create(partner_data)
        vehicle_data = {'model_id': 1, 'driver_id': new_partner.id}
        new_vehicle = self.vehicle_model.create(vehicle_data)
        self.assertEqual(new_vehicle.model_id.id, 1)
        self.assertEqual(new_vehicle.driver_id.id, new_partner.id)
        WARNING = '\033[93m'
        ENDC = '\033[0m'
        print(f"{WARNING}1. ### Test case passed{ENDC}")
