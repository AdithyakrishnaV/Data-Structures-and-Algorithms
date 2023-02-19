import math

a=int(input("enter the coefficient of x^2: \n"))
b=int(input("enter the coefficient of x: \n"))
c=int(input("enter the coefficient of constant: \n"))

d=((b*b) - (4*a*c))


if d>0:
    print("Has real and differential roots")
    n=(-b + math.sqrt(d))/(2*a)
    m=(-b + math.sqrt(d))/(2*a)
    print("Roots of the equation is: ", n,m)
elif a==0:
    print("Equation has only one solution")
    n=(-b/(2*a))
    print("Root of the equation is: ", n)
else:
    print("Equation has imaginary roots")