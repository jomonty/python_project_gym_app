import unittest
from models.gym_class import GymClass

class GymClassTest(unittest.TestCase):
    def setUp(self):
        self.test_gym_class_1 = GymClass('Erg', '2022-12-05', '07:00', 5, True)
    
    # @unittest.skip('skipped')
    def test_gym_class(self):
        self.assertEqual('Erg', self.test_gym_class_1.name)
        self.assertEqual('2022-12-05', self.test_gym_class_1.class_date)
        self.assertEqual('07:00', self.test_gym_class_1.class_time)
        self.assertEqual(5, self.test_gym_class_1.capacity)
        self.assertEqual(True, self.test_gym_class_1.is_active)