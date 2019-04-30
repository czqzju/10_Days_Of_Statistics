#https://www.hackerrank.com/challenges/s10-basic-statistics/problem

from collections import Counter

n = int(input())
arr = list(map(int, input().rstrip().split()))
arr.sort()
print("%.1f"%(sum(arr) / n))
if n % 2 == 0:
    mean = (arr[n // 2] + arr[n // 2 -1]) / 2
else:
    mean = arr[n // 2] * 1.0
print("%.1f"%(mean))

cnt = Counter(arr)

curNum = 9
curCnt = 0

for k, v in cnt.items():
    if v > curCnt:
        curCnt = v
        curNum = k
    elif v == curCnt and k < curNum:
        curCnt = v
        curNum = k
print(curNum)