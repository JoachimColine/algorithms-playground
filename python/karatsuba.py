"""
Created on Sun Jul 17 16:44:09 2022

@author: JoachimColine
"""

def nDigits(x): 
    """
    Return the number of digits in x (assuming x is an integer)
    """
    if x == 0:
        return 0
    return len(str(abs(x)))

def multiply_karatsuba(x, y):
    """
    Compute and return the Karatsuba multiplication of input integers a and b.
    """
    n = max(nDigits(x), nDigits(y))
    
    if n <= 1:
        return x * y 
    
    n2 = n // 2
    
    a = x // 10**(n2)
    b = x % 10**(n2)
    c = y // 10**(n2)
    d = y % 10**(n2)
    
    p = a + b
    q = c + d
    
    ac = multiply_karatsuba(a, c)
    bd = multiply_karatsuba(b, d)
    pq = multiply_karatsuba(p, q)
    adbc = pq - ac - bd
    
    return 10**(2 * n2) * ac + 10**n2 * adbc + bd

if __name__ == "__main__":
    x = 3141592653589793238462643383279502884197169399375105820974944592
    y = 2718281828459045235360287471352662497757247093699959574966967627
    result = multiply_karatsuba(x, y)
    result_python = x * y
    if result == result_python:
        print("Karatsuba mulitplication is a success.")
