def love_meet(bob, alice):
    print(list(set(bob).intersection(alice)))


def affair_meet(bob, alice, silvester):
    a = list(set(alice).intersection(silvester))
    print(list(set(a) - set(bob)))
