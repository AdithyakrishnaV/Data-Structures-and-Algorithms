#Tiples:- ordered, immutable, allows duplicate elements
mytuple=("adi",1, True)#brackets are optional
#or 
#mytuple="adi",1, True
mytuple=tuple(["adi",1,True,"a",'b','c'])
# print(mytuple[-2])
# if "adi" in mytuple:
#     print("yaa")
# print(mytuple.count('adi'))
# print(mytuple.count('a'))
# print(mytuple.index('a'))
a=[1,2,3,4,5,6,7,8]
*i1, i2, i3 = a

print(i1)
print(i2)
print(i3)

mydict=dict(name="Brundon",age=27,city="boston")
a=mydict["age"]
print(a)
print(mydict)
mydict["hobby"]="basketball"
print(mydict)
mydict.popitem()
print(mydict)
try:
    print(mydict["country"])
except:
    print("Error")
for key in mydict.keys():
    print(key)
print("-----------------------")
for value in mydict.values():
    print(value)
print("-----------------------")
for key, val in mydict.items():
    print(key,val)
mydict=dict(name="Brundon",age=27,city="boston")
hisdict={"name":"Rahul", "age":"22", "city":"NewYork"}
# mydict.update(hisdict)
print(mydict)
mytuple=1,2
mydict={mytuple:45}
print(mydict)