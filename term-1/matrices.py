import timeit


def matrix_sum(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        # Incorrect dimensions
        return None
    return [[sum(pair) for pair in zip(*pairs)] for pairs in zip(a, b)]


def matrix_scalar_multiplication(matrix, c):
    return [[c * x for x in row] for row in matrix]


def matrix_multiplication(a, b):
    rows_a = len(a)
    cols_a = len(a[0])
    rows_b = len(b)
    cols_b = len(b[0])

    if cols_a != rows_b:
        # Incorrect dimensions
        return None
    result = [[0 for _ in range(cols_b)]for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(rows_b):
                result[i][j] += a[i][k] * b[k][j]
    return result


def identity_matrix(n):
    res = []
    for i in range(n):
        row = [0] * n
        row[i] = 1
        res.append(row)
    return res


def matrix_transpose_naive(a):
    res = [[0 for i in range(len(a[0]))] for j in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            res[j][i] = a[i][j]
    return res


def matrix_transpose_fast(a):
    return [list(pair) for pair in zip(*b)]


def matrix_determinant(a):
    rows = len(a)
    cols = len(a[0])
    if rows != cols:
        # not square matrix
        return None
    # base case
    if rows == 2:
        return (a[0][0] * a[1][1]) - (a[0][1] * a[1][0])
    result = 0
    sign = 1
    for i in range(cols):
        tmp_matrix = []
        for i_ in range(rows):
            tmp_row = []
            for j in range(cols):
                if j != i and i_ != 0:
                    tmp_row.append(a[i_][j])
            if tmp_row:
                tmp_matrix.append(tmp_row)
        # print(tmp_matrix)
        result += sign * a[0][i] * matrix_determinant(tmp_matrix)
        sign *= -1
    return result


def matrix_inverse(a):
    pass


def is_singular_matrix(a):
    pass


def wrapper(func, *args, **kwargs):
    """Used timeit with functions that have args
    i.e. wrapped = wrapper(identity_matrix, 500)
         timeit(wrapped1, number=5)
    """
    def wrapper():
        return func(*args, **kwargs)
    return wrapper


a = [[1, 2],
     [3, 4]]
b = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
c = [[1, 0, 2, -1],
     [3, 0, 0, 5],
     [2, 1, 4, -3],
     [1, 0, 5, 0]]
# wrapped1 = wrapper(matrix_transpose_naive, b)
# print(timeit.timeit(wrapped1, number=1000))
# wrapped2 = wrapper(matrix_transpose_fast, b)
# print(timeit.timeit(wrapped2, number=1000))
print(matrix_determinant(c))
