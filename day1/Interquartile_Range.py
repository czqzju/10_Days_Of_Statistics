#https://www.hackerrank.com/challenges/s10-interquartile-range/problem
import bisect

n = int(input())
arr = list(map(int, input().rstrip().split()))
f = list(map(int, input().rstrip().split()))

q = []

for i in range(n):
    for j in range(f[i]):
        bisect.insort_right(q, arr[i])

num = len(q)

l_end = num // 2 -1
r_start = num // 2 if num % 2 == 0 else num // 2 + 1

len_child = num // 2 if num % 2 == 0 else (num - 1) // 2

if len_child % 2 == 0:
    Q1 = (q[l_end // 2] + q[l_end // 2 + 1]) / 2
    Q3 = (q[(r_start + num - 1) // 2] + q[(r_start + num - 1) // 2 + 1]) / 2
else:
    Q1 = q[l_end // 2]
    Q3 = q[(r_start + num - 1) // 2]

print("%.1f"%((Q3 - Q1) * 1.0))