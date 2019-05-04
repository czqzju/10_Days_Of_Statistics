#https://www.hackerrank.com/challenges/s10-poisson-distribution-2/problem
def EX(p):
    return p + p ** 2

x = 0.88
y = 1.55

print("%.3f" % (160 + 40 * EX(x)))
print("%.3f" % (128 + 40 * EX(y)))