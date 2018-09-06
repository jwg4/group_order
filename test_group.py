import unittest

from dihedral_8 import DIHEDRAL_8
from group import Group
from quaternion_8 import QUATERNION_8


class TestDihedralGroup(unittest.TestCase):
    def setUp(self):
        self.grp = Group(DIHEDRAL_8)

    def test_identity(self):
        e = self.grp.make(())
        self.assertEqual(str(e), "0")

    def test_ba_plus_b(self):
        ba = self.grp.make((1, 0))
        b = self.grp.make((1,))
        ca = self.grp.make((2, 0))
        self.assertEqual(ba + b, ca)

    def test_commutator_subgroup(self):
        self.assertEqual(self.grp.commutator_subgroup, [self.grp.make(()), self.grp.make((2,))])

    def test_center(self):
        self.assertEqual(self.grp.center, [self.grp.make(()), self.grp.make((2,))])

    def test_inner_automorphism_group(self):
        self.assertEqual(
            self.grp.inner_automorphism_group,
            [self.grp.make(t) for t in [(), (0,), (1,), (1, 0)]]
        )


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
        a = self.grp.make((0, ))
        self.assertEqual(ba + b, a)

    def test_commutator_subgroup(self):
        self.assertEqual(self.grp.commutator_subgroup, [self.grp.make(()), self.grp.make((2,))])

    def test_center(self):
        self.assertEqual(self.grp.center, [self.grp.make(()), self.grp.make((2,))])

    def test_inner_automorphism_group(self):
        self.assertEqual(
            self.grp.inner_automorphism_group,
            [self.grp.make(t) for t in [(), (0,), (1,), (1, 0)]]
        )

    def test_frattini_subgroup(self):
        self.assertEqual(
            self.grp.frattini_subgroup,
            [self.grp.make(()), self.grp.make((2,))]
        )
