from collections.abc import Iterable
from functools import reduce
from datetime import date
from abs_composite import AbsComposite

class Tree(Iterable, AbsComposite):

    def __init__(self, members):
        self._members = members

    def __iter__(self):
        return iter(self._members)

    def get_oldest(self):
        # recursive depth-first traverse
        def f(t1, t2):
            t1_, t2_ = t1.get_oldest(), t2.get_oldest()
            return t1_ if t1_.birthdate < t2_.birthdate else t2_
        # 1st arg - function reference
        # Now the way reduce operates, it passes pairs of items from the iterator 
        # and expects one item back. Return the oldest person from the two items
        # If either of the items my function receives is a tree itself, 
        # the function will look into that subtree to get the oldest member. 
        return reduce(f, self, NullPerson())

class NullPerson(AbsComposite):
    name = None
    birthdate = date.max

    def get_oldest(self):
        return self
