#https://www.hackerrank.com/challenges/s10-multiple-linear-regression/problem
from sklearn import linear_model
m, n = map(int, input().rstrip().split())
x = []
y = []
for _ in range(n):
    tmp = list(map(float, input().rstrip().split()))
    x.append(tmp[:m])
    y.append(tmp[m])
lm = linear_model.LinearRegression()
lm.fit(x, y)


q = int(input())
test = []
for _ in range(q):
    test.append(list(map(float, input().rstrip().split())))
res = lm.predict(test)
r = lambda f: round(f - f % 0.01 + 0.01, 2) if f % 0.01 > 0 else round(f - f % 0.01, 2)
for i in range(len(res)):
    res[i] = r(res[i])
ret = "\n".join(map(str, res))
print(ret)