## Imports:

from multiprocessing import Condition
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
    test = 600851475143
    prime_dict = {} # dict to store prime numbers
    for i in range(2,int(test**(1/2))):
        if test % i == 0 and i % 2 != 0:

            condition = True    # Holds if number can still be prime
            for num in prime_dict.values():

                if num < i**(1/2):      # if z and y both factors of x -- or zy = x -- then both numbers cannot be larger than sqrt(x)

                    if i % num == 0:
                        condition = False
                        break

            if condition == True:
                # IF the remainder of modulo division is 0 for all primes in dictionary, then add to dictionary as it is prime
                prime_dict[str(i)] = i
                ans = i



    print(f"Answer: {ans}")
    print("-"*150)


###########
def Project4(n):
    """
    For a given input n, gives the largest palindormic product of two numbers with that number of digits.

    Ex: For n = 2, largest palindromic product is 91 x 99 = 9009 
    """

    print("-"*150)
    print("\n### Project 4 ###\n")
    print(f"--> Finding largest palindromic product of two, {n}-digit numbers\n\n")
    palindrome_list = []
    for num1 in range(10**(n-1), 10**(n)):
        for num2 in range(10**(n-1), 10**(n)):
            p_condition = True
            product_str = str(num1 *num2)
            for ind in range(len(product_str)):
                if product_str[ind] != product_str[-(ind+1)]:
                    p_condition = False
            if p_condition == True:
                palindrome_list.append(int(product_str))
    palindrome_list.sort()
    ans = palindrome_list[len(palindrome_list)-1]
    print(f"Answer: {ans}")
    print("-"*150)





############
def Project5(n):
    """
    Given n, find the smallest number that is divisible by every number, 1-to-n
    """
    print("-"*150)
    print("\n### Project 5 ###\n")
    print(f"--> Finding smallest number evenly divisible by 1-through-{n}\n\n")

    condition = False
    counter = 0
    while condition == False:
        counter += 1
        for num in range(1,n+1):
            if counter % num != 0:
                condition = False
                break
            else:
                condition = True
    print(f"Answer: {counter}")
    print("-"*150)
    


###########
def Project6(n):
    """
    Given n, find difference between (n-(n-1) + n-(n-2) + ... + n)**2 and n**2 + ... + (n-(n-2))**2 + (n-(n-1))**2
    """
    print("-"*150)
    print("\n### Project 6 ###\n")
    print(f"--> Finding difference: (1+2+...{n})**2 -(1**2 +...+{n}**2) \n\n")
    l1, l2 = [], [num for num in range (1,n+1)]
    for m in range (1,n+1):
        l1.append(m**2)
    
    ans = sum(l2)**2 - sum(l1)
    print(f"Answer: {ans}")
    print("-"*150)


############
def Project7(n):
    """
    Find the nth prime number
    """

    print("-"*150)
    print("\n### Project 7 ###\n")
    print(f"--> Finding {n}th prime \n\n")

    prime_dict = {}
    next_test = 1
    while len(prime_dict.values()) < n:
        next_test += 1
        Condition = True
        for i in range(2,next_test):
            if next_test % i == 0:
                Condition = False
        
        if Condition == True:
            prime_dict[str(next_test)] = next_test

    print(f"Answer: {next_test}")
    print("-"*150)




#############
def Project8(n,m):
    """
    Find the n adjacent terms of m that have the largest product
    --> n and m both (int)
    """
    print("-"*150)
    print("\n### Project 8 ###\n")
    print(f"--> Finding largest product of {n} consecutive numbers in {m} \n\n")

    num_str = str(m)
    max_product = 0
    for i in range(0, len(num_str)-2):
        current_product = 1
        current_slice = num_str[i:i+n]
        for num in current_slice:
            current_product *= int(num)
        if current_product > max_product:
            max_product = current_product

    print(f"Answer: {max_product}")
    print("-"*150)





if __name__ == "__main__":

    n = 4

    m = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450








    Project8(13,m)