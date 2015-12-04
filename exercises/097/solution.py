def love_meet(bob, alice):
    return(list(set(bob).intersection(alice)))


def affair_meet(bob, alice, silvester):
    a = list(set(alice).intersection(silvester))
    return(list(set(a) - set(bob)))
