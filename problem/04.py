# Write a function that takes a number as input and returns True if it is prime, otherwise False.

def isPrime(num):
    if num<2:
        print(num, "is a not a prime number")
        return
        
    temp=2
    while temp<num:
        if num%temp==0:
            print(num, "is not a prime number")
            return
        temp=temp+1
        
    print(num, "is a prime number")

num=int(input("Enter number: "))
isPrime(num)