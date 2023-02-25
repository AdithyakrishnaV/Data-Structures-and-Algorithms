#collections: Counter, namedtuple, OrderedDict, defaultdict
from collections import Counter

a='abaaabbcccdddd'
b=Counter(a)
print(b)
#>>> Counter({'a': 4, 'd': 4, 'b': 3, 'c': 3})

a='abaaabbcccdddd'
b=Counter(a)
print(b.items)
#>>> dict_items([('a', 4), ('b', 3), ('c', 3), ('d', 4)])

a='abaaabbcccdddd'
b=Counter(a)
print(b.keys())
#>>>dict_keys(['a', 'b', 'c', 'd'])

a='abaaabbcccdddd'
b=Counter(a)
print(b.most_common(1)) #most common first element
#>>> [('a', 4)]

a='abaaabbcccdddd'
b=Counter(a)
print(list(b.elements()))
#>>> ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'd', 'd', 'd', 'd']

from collections import namedtuple

b=namedtuple('Point', 'x,y')
a=b(8,-1)
print(a)
#>>> Point(x=8, y=-1)

#needed before python 3.7
# it remembers the dict in correct order
from collections import OrderedDict

od=OrderedDict()
od['b']=2
od['c']=3
od['d']=4
od['a']=1
print(od)
#>>>OrderedDict([('b', 2), ('c', 3), ('d', 4), ('a', 1)])

#now 
od={}
od['b']=2
od['c']=3
od['d']=4
od['a']=1
print(od)
#>>>{'b': 2, 'c': 3, 'd': 4, 'a': 1}

#defaultdict has a default value if the key was not set
from collections import defaultdict

d=defaultdict(bool)
d['a']=1
d['b']=2
print(d['f'])
#>>> False
#if a key  with no value given the 
#default value of the type in  defaultdict is printed


#deque
from collections import deque

d=deque()

d.append(1)
d.append(2)
#append form left
d.appendleft(7)
print(d)
#pop from left
d.popleft()
print(d)
# d.clear()
print(d)
# d.extend([98,6,5,4])
d.extendleft([98,6,5,4])
print(d)
#>>>  deque([7, 1, 2])
#>>>  deque([1, 2])
#>>>  deque([1, 2])
#>>>  deque([1, 2, 98, 6, 5, 4])