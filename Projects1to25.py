## Imports:

import numpy as np
import matplotlib.pyplot as plt


###########################

# Below are the projects. At the bottom of page, simply type: "Project#()" where # is the number, and the answer will be given #

###########################

##############
def Project1():
    """
    Finds the sum of all multiples of 3 or 5 below 1000
    """
    print("-"*150)
    print("\n### Project 1 ###\n")
    print("--> Finding sum of all multiples of 3 or 5 below 1000\n\n")

    l = []  # Fill list with factors of 3 and 5

    for n in range(0,1000):

        if n % 3 == 0:
            l.append(n)
        elif n % 5 == 0:
            l.append(n)
    ans = sum(l)

    print(f"Answer: {ans}")
    print("-"*150)


##############
fib_dict  = {} # Def dictionary for fib

def fib(n):
    """
    Given index of number in fibonacci sequence, return its value
    """
    ## Update values in dictionary before returning:
    if n == 0:
        fib_dict[0]= 1
        return 1
    elif n == 1:
        fib_dict[1] = 2
        return 2
    else:
        fib_dict[n] = fib_dict[n-1] + fib_dict[n-2]
        return fib_dict[n-1] + fib_dict[n-2]

def Project2():
    """
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
    - Note this uses a dictionary and a "fib", both defined about this function
    """
    print("-"*150)
    print("\n### Project 2 ###\n")
    print("--> Finding sum of even Fibonacci terms below 4 million\n\n")

    ## Loop through integers until the next fibonacci number exceeds 4e6:
    ind  = 0 # Initial index in fib sequence
    sum_list = []
    while fib(ind) <= 4e6:
        if fib_dict[ind] % 2 == 0:
            sum_list.append(fib_dict[ind])  # only add value to sum list if it is even
        ind +=1 # Loop through until limit is exceeded

    ans = sum(sum_list)

    print(f"Answer: {ans}")
    print("-"*150)
    

##############
def Project3():
    """
    What is the largest prime factor of the number 600851475143
    - Warning this code is not well optimized and can take some time
    """
    print("-"*150)
    print("\n### Project 3 ###\n")
    print("--> Finding largest prime factor of 6000851475143\n\n")

    prime_dict = {} # dict to store prime numbers
    for i in range(2,600851475143):
        if i in (1e6, 1e7, 1e8, 1e9, 1e10, 1e11):
            print(i)
        if 600851475143 % i == 0 and i % 2 != 0:

            condition = True    # Holds if number can still be prime
            for num in prime_dict.values():

                if num < i**(1/2):      # if z and y both factors of x -- or zy = x -- then both numbers cannot be larger than sqrt(x)

                    if i % num != 0:
                        condition = False
                        break

            if condition == True:
                # IF the remainder of modulo division is 0 for all primes in dictionary, then add to dictionary as it is prime
                prime_dict[str(i)] = i

    ans = prime_dict[len(prime_dict)]

    print(f"Answer: {ans}")
    print("-"*150)





if __name__ == "__main__":

    Project3()