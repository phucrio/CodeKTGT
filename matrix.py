import numpy as np
matrix66 = np.array([
    [75, 42, 125, 125, 75, 42],
    [103, 107, 51, 76, 42, 75],
    [104, 105, 22, 75, 42, 75],
    [120, 123, 75, 42, 122, 125],
    [51, 76, 42, 75, 75, 134],
    [50, 22, 42, 106, 134, 80]
])

matrixK = np.array([
    [0, 1, 0, 0],
    [1, 0, 1, 1],
])

matrix44 = np.array([
    [47, 42, 46, 38],
    [40, 52, 57, 45],
    [23, 33, 40, 41],
    [55, 50, 43, 42]
])
matrixF = np.array([
    [0, 1, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 0, 1, 1],
    [0, 0, 1, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 0, 1, 0],
    [1, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 0, 1, 0, 1]
])

matrixJsteg = np.array([
    [1480, 49, -61, 0, 0, 0, 1, 0],
    [10, 0, 1, -22, 11, 8, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0],
    [-19, 0, 1, 27, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 1, 1, 0],
    [-30, 0, -19, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, -4, 1, 0],
    [1, 1, 0, 0, 1, 0, 1, 1]
])

matrixOutguess = np.array([
    [1480, 49, -61, 0, 0, 0, 1, 0],
    [10, 0, 1, -22, 11, 8, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0],
    [-19, 0, 1, 27, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 1, 1, 0],
    [-30, 0, -19, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, -4, 1, 0],
    [1, 1, 0, 0, 1, 0, 1, 1]
])
# matrixK = np.array([
#     [1, 1, 0],
#     [1, 1, 1],
#     [0, 1, 0]
# ])

# matrixF = np.array([
#     [1, 1, 0, 1, 1, 1],
#     [1, 1, 1, 1, 1, 0],
#     [0, 1, 0, 0, 0, 0],
#     [0, 0, 1, 0, 0, 0],
#     [1, 1, 0, 1, 1, 1],
#     [0, 1, 1, 0, 1, 0]
# ])