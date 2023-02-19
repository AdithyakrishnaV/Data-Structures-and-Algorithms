#reverse each word in a string 
s=input("Enter string to reverse:\n")
p=s.split()
for i in p:
    print(i[::-1],end=" ")