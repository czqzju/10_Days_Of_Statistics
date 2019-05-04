#https://www.hackerrank.com/challenges/s10-normal-distribution-2/problem
import math
def normal_distribution(x, u, stdd):
    return 0.5 + 0.5 * math.erf((x - u) / (stdd * 2 ** 0.5))

u = 70
stdd = 10


res1 = 1 - normal_distribution(80, u, stdd)

res2 = 1 - normal_distribution(60, u, stdd)

res3 = normal_distribution(60, u, stdd)

print("%.2f" % (res1 * 100))
print("%.2f" % (res2 * 100))
print("%.2f" % (res3 * 100))
