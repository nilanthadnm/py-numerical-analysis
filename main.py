import numpy as np


def gauss_elimination(a, b):
    """
    check matrix a and b

    :param a:coefficient matrix
    :param b:constant matrix
    :return:
    """
    # check coefficient matrix
    if a.shape[0] != a.shape[1]:
        print("ERROR: COEFFICIENT MATRIX MUST BE A SQUARE MATRIX !")
        return

    # check constant matrix
    if b.shape[1] > 1 or a.shape[0] != b.shape[0]:
        print("ERROR:NUMBER OF ROWS IN CONSTANT MATRIX IS WRONG !")
        return

    n = a.shape[0]  # gets number of rows from the coefficient matrix
    solution_vector = np.zeros(n, dtype=float)  # solution vector

    # get the augmented matrix
    # augmented_matrix = np.concatenate((a, b), axis=1)
    # print(a)

    # gauss elimination
    for k in range(n - 1):
        for j in range(k + 1, n):
            if a[j, k] == 0:
                continue
            dividing_factor = a[k][k] / a[j][k]
            for i in range(k, n):
                a[j][i] = a[k][i] - (dividing_factor * a[j][i])
            b[j] = b[k] - b[j] * dividing_factor
    print(a)
    print(b)


coefficient_matrix = np.array([[1, 1, 3], [0, 1, 3], [-1, 3, 0]], dtype=float)
constant_matrix = np.array([[1], [3], [5]], dtype=float)

gauss_elimination(coefficient_matrix, constant_matrix)
