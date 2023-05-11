from odoo.tests.common import TransactionCase

class TestLunch(TransactionCase):
    def setUp(self, *args, **kwargs):
        super(TestLunch, self).setUp(*args, **kwargs)

    def test_lunch_supplier(self):
        """test supplier creation"""
        
        partner_details =  self.env['res.partner'].create({
            'name': 'fullerton supply',
        })
        supplier = self.env['lunch.supplier'].create({
            'partner_id': partner_details.id,
            'send_by': 'phone',
            'automatic_email_time': 15,
            'tz': 'America/Los_Angeles',
        })

        self.assertEqual(supplier.send_by, 'mail')
        self.assertEqual(supplier.tz, 'America/Los_Angeles')
        self.assertEqual(supplier.partner_id, partner_details.id)  #-- supplier.partner_id.id 
        

        print("")
        print("")
        print("")
        print("------  Passed Test Case Two ------")
        print("")
        print("")
        print("")
