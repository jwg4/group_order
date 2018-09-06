def reduce_powers(element, powers, exponent=2):
    """
        >>> reduce_powers((2, 2), [[], [], []])
        ((), True)
        >>> reduce_powers((), [[], [], []])
        ((), False)
        >>> reduce_powers((2, 1, 0), [[], [], []])
        ((2, 1, 0), False)
    """
    l = []
    current = None
    count = 0
    changed = False
    for x in element[::-1]:
        if current is None:
            current = x
            count = 1
        else:
            if x == current:
                count = count + 1
                if count == exponent:
                    for g in powers[x][::-1]:
                        l.append(g)
                    count = 0
                    current = None
                    changed = True
            else:
                for i in range(0, count):
                    l.append(current)
                current = x
                count = 1
    for i in range(0, count):
        l.append(current)
    return tuple(l[::-1]), changed
    

def reduce_commutators(element, commutators):
    """
        >>> reduce_commutators((0, 1), {(0, 1): [(2, 1)], (0, 2): [], (1, 2): [] })
        ((2, 1, 0), True)
    """
    elem = list(element)
    changed = False
    for a in sorted(list(set(element))):
        count = 0
        n = []
        for i in elem:
            if i == a:
                count = count + 1
            else:
                if count > 0:
                    if a < i:
                        changed = True
                        k = (a, i)
                        for g, c in commutators[k]:
                            for f in range(0, c):
                                n.append(g)
                        n.append(i)
                        count = 1
                    else:
                        n.append(a)
                        n.append(i)
                        count = 0
                else:
                    n.append(i)
                    count = 0
        for j in range(0, count):
            n.append(a)
        elem = n
    return tuple(elem), changed

                    
def reduce(element, group):
    """
        >>> from dihedral_8 import DIHEDRAL_8
        >>> reduce((2, 2), DIHEDRAL_8)
        ()
    """
    to_change = True
    e = element
    while to_change:
        e, changed = reduce_powers(e, group['powers'])
        to_change = changed
    return e


def elements(group):
    """
        >>> from dihedral_8 import DIHEDRAL_8
        >>> elements(DIHEDRAL_8)
        [(), (0), (1), (2), (2, 1), (3, 1), (3, 2), (3, 2, 1)]
    """
    s = set()
    generators = range(0, group['n'])
    
    l = [()]
    while l:
        n = []
        for i in l:
            a = reduce(i, group)
            if a not in s:
                s.add(a)
                for g in generators:
                    n.append(a + (g,))
        l = n

    elems = list(s)
    elems.sort()
    return elems
