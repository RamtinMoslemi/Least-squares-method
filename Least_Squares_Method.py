import numpy as np
from matplotlib import pyplot as plt


def f(n):
    # create matrix X from x coordinates
    X = np.matrix([x ** i for i in range(n + 1)]).transpose()
    XTX = X.transpose() @ X
    XTy = X.transpose() @ y
    # calculate polynomial coefficients
    Beta = np.linalg.inv(XTX) @ XTy
    yHat = X @ Beta
    y_yHat = y - yHat
    MSE = y_yHat.transpose() @ y_yHat
    return np.array(Beta), MSE.item()/len(y)


def get_estimate(n, coefficients, point_x):
    point_y = 0
    for i in range(n + 1):
        point_y += coefficients[i] * point_x**i
    return point_y


def draw_graph(n, coefficients, rounding_factor=1):
    points = np.linspace(min(x) - 0.1, max(x) + 0.1, 200)
    eq = 'f_' + str(n) + '(x)= '
    for i in range(n+1):
        eq += str(np.round(coefficients[i][0], rounding_factor))
        if i == 1:
            eq += 'x'
        elif i != 0 and i != 1:
            eq += 'x^' + str(i)
        if i != n:
            eq += ' + '
    plt.title(r'$' + eq + '$')
    plt.plot(points, get_estimate(n, coefficients, points))
    plt.plot(x, y, 'r*')
    plt.grid()
    plt.show()
    print(eq, end=' ')


if __name__ == '__main__':
    y = np.matrix([1, 0, 2, -1]).transpose()
    x = np.array([1, 2, -1, 0])
    show_sol()
    show1and2()
    for degree in range(len(y)):
        Beta, MSE = f(degree)
        draw_graph(degree, Beta)
        print('\t' * 2 * (len(y) - degree), 'MSE =', MSE)
