#https://www.hackerrank.com/challenges/s10-weighted-mean/problem

n = int(input())
arr = list(map(int, input().rstrip().split()))
w = list(map(int, input().rstrip().split()))

res = 0
num = 0
for i in range(n):
    res += arr[i] * w[i]
    num += w[i]
print("%.1f"%(res / num))