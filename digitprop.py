"""
This module test the integers for the digit properties
"""

import math
def has_small_digits(n,maxdigit):
    """
    Determines whether or not the digits of `n` are all between 0 and `maxdigit`
    (inclusive).,,
    Returns `True` or `False` accordingly.
    e.g.
    has_small_digits(1021,1) returns False - third digit is larger than 1
    has_small_digits(1021,2) returns True - all digits between 0 and 2
    has_small_digits(1021,5) returns True - all digits between 0 and 5
    has_small_digits(351622,5) returns False - fourth digits if larger than 5
    has_small_digits(351622,6) returns True - all digits between 0 and 6
    """
    while n>0:
        digit = int(n%10)
        is_small_digits = True
        if(digit<=maxdigit):
            is_small_digits = True
        else:
            is_small_digits = False
            break
        n=n/10
    
    return is_small_digits

def is_antipalindrome(n):
    """
    Takes a positive integer `n`.
    Returns `True` if reversing the order of the digits in `n` gives the same
    result as replacing each digit d of `n` with 9-d ("flipping" the digits).
    Otherwise, returns `False`.
    (A number `n` for which this function returns `True` might be called an *anti
    palindrome*.)
    e.g.
    is_antipalindrome(5128) returns False, because reversing order gives 8215 whi
    le flipping digits gives 4871.
    is_antipalindrome(4815) returns True, because reversing order or flipping dig
    its each gives 5184.
    """
    temp=9999-n
    rev=0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
    if(temp==rev):
        return True
    else:
        return False  

print(is_antipalindrome(5128))