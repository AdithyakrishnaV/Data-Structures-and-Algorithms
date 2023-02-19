#In mathematics, the Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding numbers. 
#The sequence starts with 0 and 1, and then each subsequent number in the sequence is the sum of the two preceding numbers. 
#So the first few numbers in the Fibonacci sequence are:

#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610,......

# n = int(input("How many terms? "))
n=10
n1, n2= 0,1
i = 0

if n <= 0:
   print("Please enter a positive integer")

elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(n1)
else:
    for i in range (n):
       print(n1)
       m=n1+n2
       n1=n2
       n2=m




