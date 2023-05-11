from odoo.tests.common import TransactionCase

class TestLunch(TransactionCase):
    def setUp(self, *args, **kwargs):
        super(TestLunch, self).setUp(*args, **kwargs)

    def test_lunch_product(self):
        """test supplier creation"""

        sandwich_category = self.env['lunch.product.category'].create({
            'name': 'Sandwich',
        })

        pizza_place = self.env['res.partner'].create({
            'name': 'Pizza Place',
        })

        pizza_supplier = self.env['lunch.supplier'].create({
            'partner_id': pizza_place.id,
            'send_by': 'mail',
            'automatic_email_time': 11,
        })

        lunch_product = self.env['lunch.product'].create({
            'name': 'Pizza',
            'category_id': sandwich_category.id,
            'price': 15,
            'supplier_id': pizza_supplier.id,
        })

        self.assertEqual(lunch_product.category_id.id, sandwich_category.id)
        self.assertEqual(lunch_product.name, 'Pizza')
        self.assertEqual(lunch_product.price, 15)  

    

        print("")
        print("")
        print("")
        print("------  Passed Test Case one ------")
        print("")
        print("")
        print("")
