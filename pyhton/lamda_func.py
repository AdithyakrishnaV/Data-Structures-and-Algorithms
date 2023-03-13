# lambda arguments: expression
adi= lambda x: x+10
print(adi(10))
#this is same as
def adi(x):
    return x+10

# map(function,  sequence)
a=[1,2,3,4,5,6]
b=map(lambda x: x*2, a)
print(list(b))
#>>>[2, 4, 6, 8, 10, 12]

#list comperhention
c=[x*2 for x in a]
print(list(c))

# filter(function, sequence)
a=[1,2,3,4,5,6]
b=filter(lambda x: x%2==0, a)
print(list(b))
#>>>[2, 4, 6]