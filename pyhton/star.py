def space(n,i):#1 2 
    c=n-i
    if(c>0):
        print(" "*c, end="")
        i=i+1
        

def star(i):
    if(i>0):
        print("*"*(2*i-1), end="")


def start():
    n=int(input("Enter the rows: "))
    b=n
    i=1
    while n>0: #3
         #1
        space(b,i)# 1 2 3 
        star(i)
        space(b,i)
        print()
        i=i+1
        n=n-1

start()