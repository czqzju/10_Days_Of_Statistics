#https://www.hackerrank.com/challenges/s10-binomial-distribution-1/problem
import math
n, m = map(float, input().rstrip().split())

p = n / (n + m)

res = sum((math.factorial(6) / (math.factorial(i) * math.factorial(6 - i))) * (p ** i) * ((1 - p) ** (6 - i)) for i in range(3, 7))

print("%.3f"%(res))