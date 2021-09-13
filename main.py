from task1 import first_decorator
from task2 import second_decorator
from task3 import third_decorator
from task4 import fourth_decorator

# @first_decorator
# @second_decorator
# @third_decorator
@fourth_decorator
def pascal(n):
    """This function calculates the 
    elements of a pascal's triangle """
    top_row = [1]
    append_val = [0]
    
    for _ in range(n):
        print(top_row)
        top_row = [ l + r for l, r in zip(append_val+top_row, top_row+append_val)]

########################################################################################
import cmath
from math import*

# @first_decorator
# @second_decorator
# @third_decorator
# @fourth_decorator
def quad_solver(a, b, c):
    """This function solution of  the quadratic equation, given the 
    variable coefficients a, b, c. It outputs two solutions for each 
    case based on the discriminant"""
   
    discriminant = b**2 - 4*a*c

    if discriminant == 0:
        print("Roots are real and same")
        print(-b / (2*a))
        
    elif discriminant > 0:
        print("Roots are real and different ")
        print("Root 1:", (-b + sqrt(discriminant))/(2 * a))
        print("Root 2:", (-b - sqrt(discriminant))/(2 * a))
        
    else:  # discriminant<0
        print("Roots are complex")
        print("Root 1:", (- b / (2*a) + cmath.sqrt(discriminant)))
        print("Root 2:", (- b / (2*a) - cmath.sqrt(discriminant)))

########################################################################################
# @first_decorator
# @second_decorator
# @third_decorator
# @fourth_decorator
def factorial(num):
    """This function calculates the factorial of a given number"""
    res = 1
    for i in range(1, num+1):
        res = res*i
    print(res)

########################################################################################
# @first_decorator
# @second_decorator
# @third_decorator
# @fourth_decorator
def fibonacci(n):
    """This function prints the fibonacci sequence for a given number"""
    a,b = 0,1
    while b<n:
        print(b)
        a,b = b, a+b
   
########################################################################################
# @first_decorator
# @second_decorator
# @third_decorator
# @fourth_decorator
def palindromes(words):
    """This function finds out the palindromes in a given list 
    {Palindrome: a word that has the same first and last letters.}"""
    result = list(filter(lambda w: (w == "".join(reversed(w))), words))
    return result

########################################################################################
# @first_decorator
# @second_decorator
# @third_decorator
# @fourth_decorator
def multiply_by_two (x):
    """This function multiplies the given input number by two"""
    return lambda x: x*2

########################################################################################
# @first_decorator
# @second_decorator
# @third_decorator
# @fourth_decorator
def sqr(x):
    """This function gets the input number squarred"""
    return lambda x: x*x

########################################################################################
if __name__ == "__main__": 
    pascal(10, 5)
    # quad_solver(6,5,10)
    # factorial(5)
    # fibonacci(13)
    # sqr(4)
    # multiply_by_two(8)
    # palindromes(['pop', 'apple', 'bus', 'knock'])
