from math import factorial as fac
import math

def poisson(k, u):
    result = ((u ** k)*(math.e ** (-u)))/fac(k)
    return result

def calcProb(k, u, op):
    prob = 0
    if op == '=':
        prob = poisson(k, u)
    elif op == '<':
        prob = 0
        for i in range(0,k):
            prob += poisson(i, u)
    elif op == '<=':
        for i in range(0,k+1):
            prob += poisson(i, u)
    elif op == '>':
        for i in range(0,k+1):
            prob += poisson(i, u)
        prob = 1 - prob
    elif op == '>=':
        prob = 0
        for i in range(k,u+1):
            prob += poisson(i, u)
    return prob


print(calcProb(15, 20, '<'))
# print(calcProb(6, 5, '<='))

# print(poisson())