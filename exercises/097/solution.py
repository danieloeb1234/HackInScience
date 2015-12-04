def love_meet(l, m):
    return(set(l).intersection(set(m)))


def affair_meet(bob, alice, silvester):
    a = set(alice).intersection(set(silvester))
    return(set(a) - set(bob))
