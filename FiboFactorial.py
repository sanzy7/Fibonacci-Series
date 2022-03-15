#write python program to find factorial of a number
#first method using Loop
#write algorithm to find factorial of a number entered by the user

def factorial(n):
    if n<0:
        return 0

    elif n==0 or n==1:
        return 1

    else:
        f=1
        while(n>0):
            f=f*n
            n=n-1


    return f

    #Code

num=int(input('enter number'))

print("Factorial of ",num,"is",factorial(num))
    


