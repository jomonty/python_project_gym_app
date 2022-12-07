import unittest
from models.member import Member

class MemberTest(unittest.TestCase):
    def setUp(self):
        self.test_member_1 = Member('Billy', 'Biceps', False, True)
    
    # @unittest.skip('skipped')
    def test_is_member(self):
        self.assertEqual('Billy', self.test_member_1.first_name)
        self.assertEqual('Biceps', self.test_member_1.last_name)
        self.assertEqual(False, self.test_member_1.is_premium)
        self.assertEqual(True, self.test_member_1.is_active)