#https://www.hackerrank.com/challenges/s10-quartiles/problem

n = int(input())
arr = list(map(int, input().rstrip().split()))

arr.sort()

res = [0] * 3
if n % 2 == 0:
    l_end = n // 2 - 1
    r_start = n // 2
    res[1] = (arr[l_end] + arr[r_start]) // 2
    if n // 2 % 2 == 0:
        res[0] = (arr[(l_end + 1) // 2 - 1] + arr[(l_end + 1) // 2]) // 2
        res[2] = (arr[(r_start + n - 1) // 2] + arr[(r_start + n - 1) // 2 + 1]) // 2
    else:
        res[0] = arr[l_end // 2]
        res[2] = arr[(r_start + n - 1) // 2]
else:
    res[1] = arr[(n - 1) // 2]
    l_end = (n - 1) // 2 - 1
    r_start = (n - 1) // 2 + 1
    if (n - 1) // 2 % 2 == 0:
        res[0] = (arr[(l_end + 1) // 2 - 1] + arr[(l_end + 1) // 2]) // 2
        res[2] = (arr[(r_start + n - 1) // 2] + arr[(r_start + n - 1) // 2 + 1]) // 2
    else:
        res[0] = arr[l_end // 2]
        res[2] = arr[(r_start + n - 1) // 2]
print("\n".join(map(str, res)))

