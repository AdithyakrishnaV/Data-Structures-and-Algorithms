from timeit import default_timer as timer
#Stings ->  immutable, ordered, text representation

s="""hello
how 
are 
you"""
a="""hello
how 
are \
you 
doing
"""

b='''hello
how 
are 
you 
doing'''

#call by index
h="I am Adi"
i=h[0]
i=h[-1]
i=h[-2]

#reverse string
reverse=s[::-1]

# if 'i' in h:
#     print('yes')
# else:
#     print('yes')

my_string='HELLO WORLD'
#       hello world    
my_string=my_string.strip() #this will get rid of the white space
# uppercase
my_string=my_string.upper()
my_string=my_string.find('L')

# my_string=my_string.count('L') #count : 3

a_string= 'hello world'
a_string=a_string.replace('world','adi')

a_string= 'hello world'
# making list from string
a_string=a_string.split() 
# print(a_string)

#change list to string
new_string=' '.join(a_string)
# print(new_string)

start=timer()
a='a' * 6
print(a)
stop=timer()
print(stop-start)

#format string
var = "Adi"
my_string= 'hello world %s' % var
print(my_string)

#format integer
var = 1
my_string= 'hello world %d' % var
print(my_string)

#format float
var = 1.398749374
my_string= 'hello world %.2f' % var
print(my_string)



#format float
var = 1.398749374
my_string= 'hello world {:.2f}' .format(var)
print(my_string)

#format more variables  
var = 1.398749374
name= 'Adi'
my_string= 'hello world {:.2f} and {}' .format(var,name)
print(my_string)

#new way to format

var = 1.398749374
name= 'Adi'
my_string= f'Hello world {var*2} and {name}'
print(my_string)

