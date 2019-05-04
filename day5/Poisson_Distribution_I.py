#https://www.hackerrank.com/challenges/s10-poisson-distribution-1/problem
import math
p = 2.5
k = 5
print("%.3f" % ((p ** k) * (math.e ** (-1 * p)) / math.factorial(k)))