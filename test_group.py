import unittest

from dihedral_8 import DIHEDRAL_8
from group import Group

class TestDihedralGroup(unittest.TestCase):
    def setUp(self):
        self.grp = Group(DIHEDRAL_8)

    def test_ba_plus_b(self):
        ba = self.grp.make((1, 0))
        b = self.grp.make((1,))
        ca = self.grp.make((2, 0))
        self.assertEqual(ba + b, ca)

    def test_commutator_subgroup(self):
        self.assertEqual(self.grp.commutator_subgroup, [self.grp.make(()), self.grp.make((2,))])
