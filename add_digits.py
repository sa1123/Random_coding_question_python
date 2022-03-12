# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
# https://leetcode.com/problems/add-digits/

from audioop import add
import math

def add_digits(num):
    if(len(str(num)) == 1):
        return num
    sum_of_digits = 0
    while(num>0):
        sum_of_digits += num%10
        num = math.floor(num/10)
    if(len(str(sum_of_digits)) == 1):
        return sum_of_digits
    else:
        return add_digits(sum_of_digits)

print(add_digits(9999999999999))
