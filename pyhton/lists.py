# #________________________LIST_____:- ordered, mutable, allows duplicate elements
list=["adi",1,True]

list.append("cybercookie")
list.pop()
list.reverse()
# print(list)
nolist=[1,2,3,4,5,6,7,8]
# print(nolist[3:])
# print(nolist[1:6])
# print(nolist[:3])
b=nolist[::3] #every third index 
c=nolist[::-1]#reverse
print(b)

#use .copy() to copy a list other wise it will tamper the orginal list
li=nolist #both will refer to the same location
li.append("adi")
print(li)
print(nolist)
#result: 
# [1, 2, 3, 4, 5, 6, 7, 8, 'adi']
# [1, 2, 3, 4, 5, 6, 7, 8, 'adi']
li=nolist.copy()
#or 
li=nolist[:]
li.append("adi")
print(li)
print(nolist)
#result:
# [1, 2, 3, 4, 5, 6, 7, 8, 'adi']
# [1, 2, 3, 4, 5, 6, 7, 8]
