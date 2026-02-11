def fac(n):
    if n==1:
        return 1
    else:
        factorial=n*fac(n-1)
        return factorial
n=int(input("Enter your number: "))
print("Factorial of",n,"is",fac(n))
