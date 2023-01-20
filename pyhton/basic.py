#this is how we write comments
#// This is how we strike
'''
str	                      -->       Text
int, float, complex	      -->        Numeric
list, tuple, range	      -->        Sequence
dict	                  -->        Mapping
set, frozenset	          -->        Set
bool	                  -->        Boolean
bytes, bytearray,memoryview -->      Binary	        
'''
#this is how we comment multiple lines
age=20
print("my age is:"+str(age))#converted to string

#str()
#int()
#bool()
#float()
age=input("Enter number: ") #input gives a string output
print("my age is:"+age) 

#python is case sensitive 

while(True): print("pyhton") #infinite loop

command='hello world'
print(command.upper())#make everything uppercase
print(command.upper().lower())
print(command.capitalize())#first letter will be capital
#these will not modify/change our orginal command but return new string
print(command)

command='hello world'
print(command.find('w'))  #result: 6

#if we enter a string  index of the first character will be printed
command='hello world'
print(command.find('wor'))  #result: 6

command='hello world'
print(command.find('orl'))  #result: 7

command='hello world'
print(command.replace('world', 'adi'))  #result: hello adi

command='hello world'
print(command.replace('world', '345'))  #result: hello 345

# in operator
command='hello world'
print('hello' in command)  #result: True

command='hello world'
print('python' in command)  #result: False

#operators  ---------------------------------------------------

#divition
command=10 / 3
print(command)  #result: 3.3333333333333335
# a // gives an integer output
command=10 // 3
print(command)  #result: 3

#mode operator :-  returns the  reminder
command=10 % 3
print(command)  #result: 1

#multiplication
command=10 ** 3 # 10^3
print(command)  #result: 1000
command=10 * 3
print(command)  #result: 30

#boolean
command=10 >= 3
print(command)  #result: True
command=10 > 3
print(command)  #result: True
command=10 < 3
print(command)  #result: False

# and 
command=10 > 3 and 10 >= 3
print(command)  #result: True
command=10 > 3 and 10 < 3
print(command)  #result: False

#or 
command=10 > 3 or 10 < 3
print(command)  #result: True

#not 
#will inverse the result
command=not 10 < 3 # actually it is False but when using not
print(command)  #result: True

#-----------------------------------------------------------
# if condition
# python do not have {} like C , CPP etc..
# In python we use intendation
temp=30
if temp < 40:   
    print("It's cold")
else:
    print("It's hot") 
#result: It's cold

temp=40
if temp < 40:
    print("It's cold")
elif(temp > 40):
    print("It's hot") 
else:
    print("Nothing happened")
#result: Nothing happened
#-------------------------------------------------------
#loop

#while 
i=1
while(i<10):
    print(i * '*')
    i+=1 # i++ won't work in python,
         #you will get a SyntaxError: invalid syntax 
#result
'''
*
**
***
****
*****
******
*******
********
*********
'''

#for
i=1
for i in range (5):
    print(i * '*')
#result
'''
*
**
***
****
'''

#list
name=["Rahul", "Adi","Sam"]
print(name)
#result: ['Rahul', 'Adi', 'Sam']

name=["Rahul", "Adi","Sam"]
print(name[1])
#result: Adi

name=["Rahul", "Adi","Sam"]
print(name[-1])
#result: Sam

name=["Rahul", "Adi","Sam"]
name[0]="John"; # change the vlaue in index 0
print(name)
#result: ['John', 'Adi', 'Sam']

name=["Rahul", "Adi","Sam", "Sachin","Akhil"]
print(name[1:4])
#result: ['Adi', 'Sam', 'Sachin']

#list methods ---------------------------------------

#append
num=[1,2,3,4,5,6]
num.append(8)
print(num)
#result: [1, 2, 3, 4, 5, 6, 8]

#insert
num=[1,2,3,4,5,6,8]
num.insert(2,4)
print(num)
#result: [1, 2, 4, 3, 4, 5, 6, 8]
#here 4 is inserted at the second index

#remove
num=[1,2,3,4,5,6,8]
num.remove(8)
print(num)
#result: [1, 2, 4, 3, 4, 5, 6]
#if we remove a number not in the list we get a ValueError
num=[1,2,3,4,5,6,8]
num.remove(0)
print(num)

#ValueError: list.remove(x): x not in list

#clear
num=[1,2,3,4,5,6,8]
num.clear()
print(num)
#result: []

# in
num=[1,2,3,4,5,6,8]
print(1 in num)
#result: True

num=[1,2,3,4,5,6,8]

## len
# find the number of items
print(len(num))
#result: 7

#-------------------------------------------
#loop through the items in the list
#for loop
num=[1,2,3,4,5,6,8]
for item in num:
    print(item)
'''
result: 
1
2
3
4
5
6
8
'''

#while loop
num=[1,2,3,4,5,6,8]
i=0
while i< len(num):
    print(num[i])
    i+=1
'''
result: 
1
2
3
4
5
6
8
'''

#range() function
num = range(5)
print(num)
#result: range(0, 5)

num = range(5)
for n in num:
    print(n)
'''
result: 
0
1
2
3
4
'''

num = range(5, 10)
for n in num:
    print(n)
'''
result: 
5
6
7
8
9
''' 

num = range(5, 10, 2)
for n in num:
    print(n)
'''
result: 
5
7
9
'''

num = range(5, 10, 3)
for n in num:
    print(n)
'''
result: 
5
8
'''

for n in range(5):
    print(n)
'''
result: 
0
1
2
3
4
'''

#Tuple

#tuples are immutable, we cannot change or modify it
num=[1,2,3,4]# this is a list
num=(1,2,3,4)# this is a tuple

num=(1,2,3,4)
num[3]=6
print(num)

#TypeError: 'tuple' object does not support item assignment

 