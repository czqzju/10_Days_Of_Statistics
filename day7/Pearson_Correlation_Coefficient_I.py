#https://www.hackerrank.com/challenges/s10-pearson-correlation-coefficient/problem
import math

n = int(input())
x = list(map(float, input().rstrip().split()))
y = list(map(float, input().rstrip().split()))

xu = sum(item for item in x) / n
x_stdd = (sum((item - xu) ** 2 for item in x) / n) ** 0.5

yu = sum(item for item in y) / n
y_stdd = (sum((item - yu) ** 2 for item in y) / n) ** 0.5

res = round(sum((x[i] - xu) * (y[i] - yu) for i in range(n)) / (n * x_stdd * y_stdd), 3)

print(res)