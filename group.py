from collections import defaultdict

from representation import elements, reduce


ALPHA = "abcdefghijklmno"


def element_class(group):

    class Element(object):
        _neg = None

        def __init__(self, t):
            self.representation = t

        def __str__(self):
            if not self.representation:
                return "0"
            return "".join([ALPHA[i] for i in self.representation])

        def __repr__(self):
            return "Element %s of Group %s" % (self.representation, repr(group))

        def __hash__(self):
            return hash(group) + hash(self.representation)

        def __cmp__(self, other):
            return cmp(self.representation, other.representation)

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

    def __init__(self, spec):
        self.spec = spec
        self.cls = element_class(self)
        self._table = defaultdict(lambda : None)

    def make(self, t):
        return self.cls(t)

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
        return sorted(list(set(self._commutators)))

    @property
    def _commutators(self):
        for i in self.elements:
            i_inv = -i
            for j in self.elements:
                if i != j:
                    j_inv = -j
                    yield i + j + i_inv + j_inv

    @property
    def center(self):
        return sorted(list(self._center))

    @property
    def _center(self):
        for i in self.elements:
            if all(i + x == x + i for x in self.elements):
                yield i

    @property
    def inner_automorphism_group(self):
        return sorted(list(self._inner_automorphism_group))

    @property
    def _inner_automorphism_group(self):
        d = defaultdict(list)
        for i in self.elements:
            i_inv = -i
            k = tuple(i_inv + x + i for x in self.elements)
            d[k].append(i)

        for k in d:
            l = sorted(d[k])
            yield l[0]

    @property
    def squares(self):
        return sorted(list(set( a + a for a in self.elements)))

    @property
    def frattini_subgroup(self):
        return sorted(list(set(self._frattini_subgroup)))

    @property
    def _frattini_subgroup(self):
        for a in self.commutator_subgroup:
            for b in self.squares:
                yield a + b
