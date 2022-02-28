 import imp

from initialize_functions import *

'''
To use a function, you call it. When you call a function, you must provide values, or arguments, for each of the function’s parameters.
Functions allow you to write code efficiently. When you need to perform an action more than once, wrap that code in a function and call it when you need it. When you need to change how the action is carried out, you can change the code in the function, and the improvement is applied everywhere.
'''

print("Invoking zero arg function")
zero_arg_function()

print("Invoking function with required arguments")
introduction("Harry", "Houdini")

print("Invoking function with default arguments")
introduction_with_default_args()

#TODO: In this file, go ahead and invoke the rest of the functions from the initialize_functions.py file

print('invoking function with mix of default arguments')
introduction_with_mix_of_default_args('john')

print('invoking function with product of two numbers')
product_of_two_num(5,7)

print('invoking function adding all numbers')
add_all_nums(2,3,4)

print('invoking function doubling a number')
double(4)

print('invoking function fibonacci numbers')
fib(3)

print('invoking function to subtract numbers')
subtract(5,3)

