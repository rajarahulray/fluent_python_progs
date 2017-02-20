# -*- coding: utf-8 -*-
import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
 ranks = [str(n) for n in range(2, 11)] + list('JQKA')
 suits = 'spades diamonds clubs hearts'.split()

 def __init__(self):
     self._cards = [Card(rank, suit) for suit in self.suits
                    for rank in self.ranks]
 def __len__(self):
     return len(self._cards)
 def __getitem__(self, position):
     return self._cards[position]

     
     
#Some quicks in Python....
#list element access alongwith their indices...
l = [1,2,3,4,5,6];

for index, element in enumerate(l):
    print("Index", index, ":", "element at l[{}]".format(index), element);