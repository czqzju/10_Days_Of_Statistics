#https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-1/problem
import math
def normal_distribution(x, u, stdd):
    return 0.5 + 0.5 * math.erf((x - u) / (stdd * 2 ** 0.5))

if __name__ == "__main__":
    u = 205 * 49
    stdd = 15 * 49 ** 0.5
    print(round(normal_distribution(9800, u, stdd), 4))
