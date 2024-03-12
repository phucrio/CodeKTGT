import numpy as np
from total import *
from matrix import *
# Tạo các ma trận mẫu
matrix_A = np.array([
    [1, 0, 1],
    [0, 1, 0],
    [1, 1, 1]
])

matrix_B = np.array([
    [0, 1, 0],
    [1, 0, 1],
    [1, 0, 0]
])

# Thực hiện phép XOR giữa hai ma trận
result_matrix = np.bitwise_xor(matrix_A, matrix_B)

# Hiển thị ma trận kết quả
# print(sum(sum(result_matrix)))




og = Outguess(matrixJsteg)   
m="01101011"
og.run(m,k=3,shiftcol=1)
# og.hide(mt2,m)