#https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-3/problem

if __name__ == "__main__":
    n = 100
    u = 500
    stdd = 80
    p = 0.95
    z_score = 1.96

    stdErr = stdd / (n ** 0.5)

    marginErr = stdErr * z_score

    A = u - marginErr
    B = u + marginErr

    print(round(A, 2))
    print(round(B, 2))
