import numpy as np
from matplotlib import pyplot as plt


def f(degree):
    # create the design matrix from x coordinates
    design_matrix = np.matrix([x ** i for i in range(degree + 1)]).transpose()
    # figure out the polynomial coefficients
    parameter_vector = np.linalg.inv(design_matrix.transpose() @ design_matrix) @ design_matrix.transpose() @ y
    # calculate the residual vector
    residual_vector = y - design_matrix @ parameter_vector
    # compute the Mean Squared Error
    mean_squared_error = (residual_vector.transpose() @ residual_vector).item() / n
    # return the coefficients and the MSE
    return np.array(parameter_vector), mean_squared_error


# return the estimated value of output y given input x
def get_estimate(degree, coefficients, point_x):
    point_y = 0
    for i in range(degree + 1):
        point_y += coefficients[i] * point_x ** i
    return point_y


def get_equation_str(degree, coefficients, mse, rounding_factor):
    eq = 'f_' + str(degree) + '(x)= '
    for i in range(degree + 1):
        eq += str(np.round(coefficients[i][0], rounding_factor))
        if i == 1:
            eq += 'x'
        elif i != 0 and i != 1:
            eq += 'x^' + str(i)
        if i != degree:
            eq += ' + '
    eq += 3 * '\;' + 'MSE=' + str(np.round(mse, rounding_factor))
    return eq


def draw_graph(degree, coefficients, mse, rounding_factor=3):
    # set the points up
    points = np.linspace(min(x) - 0.1, max(x) + 0.1, 200)
    # get the equation string
    eq = get_equation_str(degree, coefficients, mse, rounding_factor)
    # add the title to the plot
    plt.title(r'$' + eq + '$')
    # add the original inputs and outputs to the plot
    plt.plot(x, y, 'r*')
    # draw the graph of our estimation
    plt.plot(points, get_estimate(degree, coefficients, points))
    # add grid to the plot
    plt.grid()
    # show the plot
    plt.show()


if __name__ == '__main__':
    # take in the number of inputs and outputs
    n = int(input('Enter the number of inputs: '))
    # create the x vector
    x = np.array([int(i) for i in input('enter the inputs: ').split()])
    # create the y vector
    y = np.matrix([int(i) for i in input('enter the outputs: ').split()]).transpose()
    # find f_n for every n
    for j in range(n):
        Beta, MSE = f(j)
        draw_graph(j, Beta, MSE)
