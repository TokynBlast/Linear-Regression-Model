X_ = (1, 2, 3, 4, 5, 6, 7, 8)
y =  (1, 2, 4, 5, 7, 8, 10, 11)
x = 9.5
n = len(X_)

def m(X_, y):
    sum_X_SQR = 0
    sum_X_Y = 0

    for i in range(n):
        sum_X_SQR += X_[i] ** 2
        sum_X_Y += X_[i] * y[i]

    return (n * sum_X_Y - sum(X_) * sum(y)) / (n * sum_X_SQR - sum(X_) ** 2)

def b(x, y, slope):
    return (sum(y) - slope * sum(x)) / n

def regress():
    slope = m(X_, y)
    intercept = b(X_, y, slope)
    return slope * x + intercept

print(regress())
