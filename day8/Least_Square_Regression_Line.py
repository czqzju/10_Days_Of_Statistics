#https://www.hackerrank.com/challenges/s10-least-square-regression-line/problem
x = [95, 85, 80, 70, 60]
y = [85, 95, 70, 65, 70]
n = 5
multiply_sum = 0
x_sum = 0
y_sum = 0
x_square_sum = 0
for i in range(n):
    multiply_sum += x[i] * y[i]
    x_sum += x[i]
    y_sum += y[i]
    x_square_sum += x[i] ** 2

b = (n * multiply_sum - x_sum * y_sum) / (n * x_square_sum - x_sum ** 2)
a = y_sum / n - b * x_sum / n

res = round(a + b * 80, 3)

print(res)