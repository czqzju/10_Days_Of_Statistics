#https://www.hackerrank.com/challenges/s10-binomial-distribution-2/problem
import math

def computeC_n_x(n, x):
    return math.factorial(n) / (math.factorial(x) * math.factorial(n - x))

def binomial(n, start, end, p):
    return sum(computeC_n_x(n, i) * p ** i * (1 - p) ** (n - i) for i in range(start, end))


p = 0.12

no_more_than_2 = binomial(10, 0, 2, p)
at_least_2 = binomial(10, 2, 11, p)

print("%.3f" % (no_more_than_2))
print("%.3f" % (at_least_2))