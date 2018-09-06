from collections import defaultdict

from representation import elements, reduce


ALPHA = "abcdefghijklmno"


def element_class(group):

    class Element(object):
        _neg = None

        def __init__(self, t):
            self.representation = t

        def __str__(self):
            return "".join([ALPHA[i] for i in self.representation])

        def __eq__(self, other):
            return self.representation == other.representation

        def __add__(self, y):
            return group.add(self.representation, y.representation)

        def __neg__(self):
            if not self._neg:
                for i in group.elements:
                    if self + i == Element(()):
                        self._neg = i
                        break
                else:
                    raise Exception("could not find inverse of %s" % (self, ))
            return self._neg

    return Element


class Group(object):
    _elements = None
    _table = defaultdict(lambda : None)

    def __init__(self, spec):
        self.spec = spec

        self.cls = element_class(self)

    def add(self, x, y):
        if not self._table[(x, y)]:
            self._table[(x, y)] = reduce(x + y, self.spec)
        return self.cls(self._table[(x, y)])

    @property
    def elements(self):
        if not self._elements:
            self._elements = [ self.cls(e) for e in elements(self.spec) ]
        return self._elements
        
    @property
    def commutator_subgroup(self):
        return list(set(self._commutators))

    @property
    def _commutators(self):
        for i in self.elements:
            i_inv = -i
            for j in self.elements:
                if i != j:
                    j_inv = -j
                    yield i + j + i_inv + j_inv
