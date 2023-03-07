#iterloops : product, permutation, combinations, accumulate, count, cycle, repeat

#product
from itertools import product
a=[1,2]
b=[3,4]

pro=product(a,b)
print(list(pro))
#>>> [(1, 3), (1, 4), (2, 3), (2, 4)]

a=[1,2]
b=[3]
pro=product(a,b,repeat=2)
print(list(pro))
#>>>  [(1, 3, 1, 3), (1, 3, 2, 3), (2, 3, 1, 3), (2, 3, 2, 3)]


# A permutation is an arrangement of objects in a definite order
from itertools import permutations

a=[1,2]
per=permutations(a)
print(list(per))
#>>> [(1, 2), (2, 1)]

a=[1,2,3,4,5,6]
per=permutations(a,2) #length will be 2 eg: [(1, 2), (1, 3), (1, 4),...]
print(list(per))


#A combination is a mathematical technique that determines the number of possible arrangements in a collection of items where the order of the selection does not matter

#no repetition
from itertools import combinations

a=[1,2,3,4,5,6]
comb=combinations(a,2)
print(list(comb))
#>>> [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 3), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6), (4, 5), (4, 6), (5, 6)]

#if repetition needed 
from itertools import combinations , combinations_with_replacement
a=[1,2,3,4,5,6]
comb_r=combinations_with_replacement(a,2)
print(list(comb_r))
#>>> [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 3), (3, 4), (3, 5), (3, 6), (4, 4), (4, 5), (4, 6), (5, 5), (5, 6), (6, 6)]


#accumulate
from itertools import  accumulate

a=[1,2,3,4,5,6]
acc=accumulate(a)
print(list(acc))
#>>> [1, 3, 6, 10, 15, 21]

#to multiply
import operator
a=[1,2,3,4,5,6]

acc=accumulate(a, func=operator.mul)
print(list(acc))
#>>> [1, 2, 6, 24, 120, 720]

#count, cycle, repeat
from itertools import  count ,cycle,repeat

for i in count(10):
    print(i)
    if i ==20:
        break

for i in repeat(3, 20):
    print(i)

a=[1,2,3]
for i in cycle (a):
    print(i)