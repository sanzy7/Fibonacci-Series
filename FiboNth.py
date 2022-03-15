##Fibonacci sequence where nth term is the sum of (n-1)th and (n-2)th term.
n = int(input("How many terms do you want?  "))
# Initializing the first two terms
n1 = 0
n2 = 1

count = 0

if n <=0 :
    print ("Please enter a number greater than 0.")

else:
    print("Fibonacci sequence:")
    while count < n:
        print(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1
        