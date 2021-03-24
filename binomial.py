# PURPOSE: Take in n, p, k vals and performs a binomial calculation to solve a problem
import numpy as np

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

def binomial(n,p,k, op):
    q = round(1 - p,4)
    choose = (factorial(n)/(factorial(k)*factorial(n-k)))
    if op == '=':
        prob = round(float(choose * (p ** k) * (q ** (n-k))),4)
    elif op == '<':
        prob = 0
        for i in range(0,k):
            prob += round(float(choose * (p ** k) * (q ** (n-k))),4)
    elif op == '<=':
        prob = 0
        for i in range(0,k+1):
            prob += round(float(choose * (p ** k) * (q ** (n-k))),4)
    elif op == '>':
        prob = 0
        for i in range(k+1,n):
            prob += round(float(choose * (p ** k) * (q ** (n-k))),4)
    elif op == '>=':
        print('greater than or equal to')
        prob = 0
        for i in range(k,n+1):
            print(i)
            print(str(float(choose * (p ** i) * (q ** (n-i)))))
            prob += float(choose * (p ** i) * (q ** (n-i)))
    return prob

try:
    n = int(input("Enter the sample space: "))
    p = float(input("Enter the probability of success: "))
    k = int(input("Enter how many successes: "))
    op = input("Enter an operation: ")
    ans = binomial(n,p,k, op)
    print("The answer is: " + str(ans))
except ValueError:
    print('ERROR: Incorrect value type inputted.')
# print(binomial(5,0.8,3))
# print("%0.1f" % (1.0-0.8))



