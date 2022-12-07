import unittest
from datetime import date, time
from models.gym_class import GymClass

class GymClassTest(unittest.TestCase):
    def setUp(self):
        self.test_gym_class_1 = GymClass('Erg', date(2022, 12, 5), time(7,0,0), 5, True)
    
    # @unittest.skip('skipped')
    def test_gym_class(self):
        self.assertEqual('Erg', self.test_gym_class_1.name)
        self.assertEqual(date(2022, 12, 5), self.test_gym_class_1.class_date)
        self.assertEqual(time(7,0,0), self.test_gym_class_1.class_time)
        self.assertEqual(5, self.test_gym_class_1.capacity)
        self.assertEqual(True, self.test_gym_class_1.is_active)