def reduce_powers(element, powers, exponent=2):
    """
        >>> from dihedral_8 import DIHEDRAL_8
        >>> reduce_powers((2, 2), DIHEDRAL_8)
        (), True
    """
    l = []
    current = None
    count = 0
    changed = True
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
    return l[::-1], changed
    

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
