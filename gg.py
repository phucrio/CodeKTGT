import math 
from colorama import Fore, Style
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'
def matrix_to_array(matrix):
    array = []
    for row in matrix:
        array.extend(row)
    return array
    
def array_to_matrix(array, m, n):
    if m * n != len(array):
        print("Số lượng phần tử của mảng không phù hợp với số hàng và số cột đã cho.")
        return None
    
    matrix = []
    for i in range(m):
        row = array[i * n:(i + 1) * n]
        matrix.append(row)
    return matrix
def print_matrix(matrix):

    num_rows = len(matrix)
    num_cols = len(matrix[0])
    
    max_widths = [max([len(str(matrix[i][j])) for i in range(num_rows)]) for j in range(num_cols)]
    
    print("-------------------------------------")
    for i in range(num_rows):
        for j in range(num_cols):
            print(str(matrix[i][j]).rjust(max_widths[j]), end="  ")
        print()
    print("-------------------------------------")

def print_embbed_matrix(matrix, l):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    
    max_widths = [max([len(str(matrix[i][j])) for i in range(num_rows)]) for j in range(num_cols)]
    
    print("-------------------------------------")
    for i in range(num_rows):
        for j in range(num_cols):
            if l > 0:
                print(f'{RED}{str(matrix[i][j]).rjust(max_widths[j])}{RESET}', end="  ")
                l -= 1
            else:
                print(str(matrix[i][j]).rjust(max_widths[j]), end="  ")
        print()
    print("-------------------------------------")
    
def print_embbed_matrix_img(matrix, l):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    
    max_widths = [max([len(str(matrix[i][j])) for i in range(num_rows)]) for j in range(num_cols)]
    
    print("-------------------------------------")
    k = 1
    for i in range(num_rows):
        for j in range(num_cols):
            if k in l:
                print(f'{RED}{str(matrix[i][j]).rjust(max_widths[j])}{RESET}', end="  ")
            else:
                print(str(matrix[i][j]).rjust(max_widths[j]), end="  ")
            k +=1
        print()
    print("-------------------------------------")
    
def test():
    # Example usage:
    array = [1, 2, 3, 4, 5, 6]
    m = 2
    n = 3
    result = array_to_matrix(array, m, n)
    print(result)

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = matrix_to_array(matrix)
    print(result)
    
    matrix = [[1, 2, 3,4], [4, 5, 6,4], [7, 8, 9,4]]
    print_matrix(matrix)

