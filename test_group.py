import unittest

from dihedral_8 import DIHEDRAL_8
from group import Group
from quaternion_8 import QUATERNION_8


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


class TestQuaternionGroup(unittest.TestCase):
    def setUp(self):
        self.grp = Group(QUATERNION_8)

    def test_inverse_of_a(self):
        a = self.grp.make((0, ))
        ca = self.grp.make((2, 0))
        self.assertEqual(-a, ca)

    def test_ba_plus_b(self):
        ba = self.grp.make((1, 0))
        b = self.grp.make((1,))
        ca = self.grp.make((2, 0))
        self.assertEqual(ba + b, ca)

    def test_commutator_subgroup(self):
        self.assertEqual(self.grp.commutator_subgroup, [self.grp.make(()), self.grp.make((2,))])
