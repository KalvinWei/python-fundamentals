# python comment format: hashtag + space + comment content

# next line is to import math python module to enable us utilize more advanced arithmetic functions
from math import *

# ---------------SECTION 1: BASICS------------------

# print, string and string operations
print("Hello,world")
my_name = "john"
print("Hello," + my_name)
print("Giraffe\n\"Academy\"")  # use backslash(\) to escape
print("convert this to uppercase".upper())
print("should be True for this line".upper().isupper())
print(len("this should be outputting the length of this sentence"))
a_word = "get the first letter of this sentence"
print(a_word[0])  # index begins from 0
print(a_word.replace("first", "second"))  # this should be print the result of a partially replaced sentence

# numbers and booleans
my_age = 50
my_health_degree = 80.45
is_male = True  # in capital letter!!!

# arithmetic operations supported
print(10 % 3)  # remainder
print(10 / 3)  # quotient
print(str(5))  # convert numbers into strings
print("my age is " + str(5))
print("5's 2nd power is " + str(pow(5, 2)))
print("Max in [4,5] is " + str(max(4, 5)))

# if we want to use advanced arithmetic functions, we must import the correspondent python library
# it's done the header of this file
print("ceiling of 4.57 is " + str(ceil(4.57)))
print("floor of 4.57 is " + str(floor(4.57)))
print(sqrt(9))


