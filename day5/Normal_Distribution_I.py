#https://www.hackerrank.com/challenges/s10-normal-distribution-1/problem
import math
x = 19.5


def normal_distribution(x, u, stdd):
    return 0.5 + 0.5 * math.erf((x - u) / (stdd * 2 ** 0.5))

if __name__ == "__main__":
    x1 = 20
    x2 = 22
    res1 = normal_distribution(x, 20, 2)
    res2 = normal_distribution(x2, 20, 2) - normal_distribution(x1, 20, 2)

    print("%.3f" % res1)
    print("%.3f" % res2)