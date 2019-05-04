#https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-2/problem
import math

def N(x, u, stdd):
    return 0.5 + 0.5 * math.erf((x - u) / (stdd * 2 ** 0.5))

if __name__ == "__main__":
    u = 2.4 * 100
    stdd = 2.0 * 100 ** 0.5
    print(round(N(250, u, stdd), 4))