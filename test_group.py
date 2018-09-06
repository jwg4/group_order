import unittest

from dihedral_8 import DIHEDRAL_8
from group import Group

class TestDihedralGroup(unittest.TestCase):
    def setUp(self):
        self.grp = Group(DIHEDRAL_8)

    def test_commutator_subgroup(self):
        self.assertEqual(self.grp.commutator_subgroup, [(), (2)])
