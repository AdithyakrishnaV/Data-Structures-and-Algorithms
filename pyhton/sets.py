# #Sets - unordered, mutable, no duplicates

# # myset={1,2,3,4}
# # myset=set([1,2,3,4])

# #create an empty set
# s=set()

# s.add(1)
# s.add(3)
# s.add(4)

# # s.discard(3)
# print(s.pop())
# # s.clear() #clear all elements from the set
# # s.remove(5) 
# # # KeyError: 5  when given a number not in the set
# print(s)

# odd=set([0,1,3,5])
# even=set([2,4,6])
# even=set([1,2,3,4,5])
# #find union in built  feature
# u=odd.union(even)
# #find intersection in built  feature
# a=odd.intersection(even)

# print(u)
# print(a)
# setA={1,2,3,4,5,6,7,8,9,10}
# setB={2,4,6,8,9}
# diff=setA.difference(setB)
# #{1, 3, 5, 7, 10}
# print(diff)
# dif=setB.difference(setA)
# #set()

# setA={1,2,3,4,5,6,7,8,9,10}
# setB={2,4,6,8,9}
# m=setB.issubset(setA)
# print(m)
# #true

# setA={1,2,3,4,5,6,7,8,9,10}
# setB={2,4,6,8,9}
# m=setB.issuperset(setA)
# print(m)
# #False

# setA={1,2,3,4,5,6,7,8,9,10}
# #setB=setA.copy()
# #or
# setB=set(setA)

# setB.add(100)
# print(setA)
# print(setB)
# #result:
#     # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
#     # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100}
