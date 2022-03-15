# Program to display the Fibonnaci sequence upto n-th term

# Need integer input from user. and convert to integer type
num=int(input("Enter any number: "))

# declare 2 variables, and initiatilize them with 0 and 1
n1, n2 = 0, 1

# Fibo series is calculated by addition of preceeding 2 numbers
# Declare one variale sum which will store the addition value, initially set it to zero
sum =0

#add validation to number. if number entered by user is 0 or less than 1, give error msg
if num<=0:
    print("Please enter number greater than 0")
else:
    for i in range(0, num):   #to print nth term from series, write For Loop with range function, starting from zero to num
        print(sum, end=" ")  #print initial sum value
        n1 = n2  #second number will be considered first value and sum value will be considered second number
        n2 = sum  #for every iteration, n2 will be stored in n1, adn sum value will be stores in n2
        sum = n1 + n2 #this process with add preceeding 2 numbers and process will cotninue until condition is satsifed

 
