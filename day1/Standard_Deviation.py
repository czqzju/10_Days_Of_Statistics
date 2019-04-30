#https://www.hackerrank.com/challenges/s10-standard-deviation/problem

n = int(input())
arr = list(map(int, input().rstrip().split()))

u = sum(arr) / n

res = (sum((arr[i] - u) ** 2 for i in range(n)) / n) ** 0.5

print("%.1f" % (res))