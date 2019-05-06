#https://www.hackerrank.com/challenges/s10-spearman-rank-correlation-coefficient/problem
n = int(input())
x = list(map(float, input().rstrip().split()))
y = list(map(float, input().rstrip().split()))

sort_x = sorted(x)
sort_y = sorted(y)

dict_x = dict()
dict_y = dict()

for i in range(n):
    dict_x.setdefault(sort_x[i], i)
    dict_y.setdefault(sort_y[i], i)

di_square = sum((dict_x[x[i]] - dict_y[y[i]]) ** 2 for i in range(n))
res = round((1 - 6 * di_square / (n * (n ** 2 - 1))), 3)

print(res)