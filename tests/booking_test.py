import unittest
from datetime import date, time
from models.booking import Booking
from models.member import Member
from models.gym_class import GymClass

class BookingTest(unittest.TestCase):
    def setUp(self):
        self.test_member_1 = Member('Billy', 'Biceps', False, True)
        self.test_gym_class_1 = GymClass('Erg', date(2022, 12, 5), time(7,0,0), 5, True)
        self.booking_1 = Booking(self.test_gym_class_1, self.test_member_1)
    
    # @unittest.skip('skipped')
    def test_is_booking(self):
        self.assertEqual('Billy', self.booking_1.member.first_name)
        self.assertEqual('Erg', self.booking_1.gym_class.name)