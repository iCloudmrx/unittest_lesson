import unittest
from INKAPSULYATSIYA import Auto


class CarTest(unittest.TestCase):
    def setUp(self):
        self.make = "GM"
        self.model = "malibu"
        self.color = "black"
        self.year = 2022
        self.price = 30000
        self.km = 10000
        self.auto1 = Auto(self.make, self.model, self.color, self.year)
        self.auto2 = Auto(self.make, self.model, self.color, self.year,
                          self.price)

    def test_create(self):
        # Qiymatlarni mavjudligini AssertIsNotNone bilan tekshiradi
        self.assertIsNotNone(self.auto1.make)
        self.assertEqual(self.make, self.auto1.make)
        self.assertIsNotNone(self.auto1.modul)
        self.assertEqual(self.model, self.auto1.modul)
        self.assertIsNotNone(self.auto1.year)
        self.assertEqual(self.year, self.auto1.year)
        self.assertIsNotNone(self.auto1.color)
        self.assertEqual(self.color, self.auto1.color)
        # Qiymat majud emasligin AssertIsNone bilan tekshiradi
        self.assertIsNone(self.auto1.price)
        # qiymat tengligini assertEqual bilan tekshiradi
        self.assertEqual(0, self.auto2.get_km())
        self.assertEqual(4, self.auto1.get_num_auto())
        self.assertEqual(self.price, self.auto2.price)

    def test_set_price(self):
        new_price = 40000
        self.auto2.narx = new_price
        self.assertEqual(new_price, self.auto2.narx)

    def test_add_kam(self):
        # 1 musbat qiymat uchun test
        self.auto1.add_km(self.km)
        self.assertEqual(self.km, self.auto1.get_km())
        km = 5000
        self.auto1.add_km(km)
        self.assertEqual(15000, self.auto1.get_km())
        # 2 manfiy qiymat berib ko'ramiz
        new_km = -50000
        try:
            self.auto1.add_km(new_km)
            self.assertEqual(self.km, self.auto1.get_km)
        except ValueError as error:
            self.assertEqual(type(error), ValueError)


unittest.main()
