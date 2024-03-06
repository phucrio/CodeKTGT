from gg import array_to_matrix,matrix_to_array,print_matrix,print_embbed_matrix,print_embbed_matrix_img
import numpy as np
from colorama import Fore, Style
from matrix import matrix66,matrixK,matrixF
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

def shift_k_bit(k, matrix, right=1):
    arr = matrix_to_array(matrix)
    if right: 
        newarr = arr[-k:] + arr[:-k]
    else:
        newarr = arr[k:] + arr[:k]
    new_matrix = array_to_matrix(newarr,len(matrix),len(matrix[0]))
    return new_matrix

def shift_k_columns(k, matrix, right=1):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    new_matrix = [[0] * num_cols for _ in range(num_rows)]

    for i in range(num_rows):
        for j in range(num_cols):
            if right:
                new_col = (j + k) % num_cols
            else:
                new_col = (j - k) % num_cols
            new_matrix[i][new_col] = matrix[i][j]

    return new_matrix




def zigzag(matrix):
    rows, cols = len(matrix),len(matrix[0])
    output = []
    r, c = 0, 0
    for _ in range(rows * cols):
        output.append(matrix[r, c])
        if (r + c) % 2 == 0:  # Di chuyển lên trên
            if c == cols - 1:
                r += 1
            elif r == 0:
                c += 1
            else:
                r -= 1
                c += 1
        else:  # Di chuyển xuống dưới
            if r == rows - 1:
                c += 1
            elif c == 0:
                r += 1
            else:
                r += 1
                c -= 1
    return output
def undomix_matrix(matrix_A, matrix_B):
    row = len(matrix_A)
    col = len(matrix_A[0])
    arr = [0]*row*col
    for i in range(row):
        for j in range(col): 
            arr[matrix_A[i][j]-1] = matrix_B[i][j]
    newmatrix = array_to_matrix(arr,row,col)
    return newmatrix

def random_hide_and_seek(matrix ,m : str,a : int,p=37):
    print("Ma tran ban dau")
    print_matrix(matrix)
    arr = []
    for i in range(1,p,1):
        arr.append(pow(a,i,p))
    random_matrix = array_to_matrix(arr,len(matrix),(len(matrix[0])))
    print("\nMa tran xao tron")
    print_matrix(random_matrix)
    matrix_arr = matrix_to_array(matrix)
    temparr = []
    
    for x in arr:
        temparr.append(matrix_arr[x-1])
    
    after_random_matrix = array_to_matrix(temparr,len(matrix),len(matrix[0]))
    print("\nMa tran sau xao tron")
    print_matrix(after_random_matrix)
    
    for x in range(len(m)):
        if int(m[x]) == 0 and temparr[x] % 2 == 1:
            temparr[x] -= 1
        elif int(m[x]) == 1 and temparr[x] % 2 == 0: 
            temparr[x] += 1
    
    embbed_matrix = array_to_matrix(temparr,len(matrix),len(matrix[0]))
    print(f"\nMa tran nhung m={m}")
    print_embbed_matrix(embbed_matrix,len(m))
    
    print("\nMa tran anh sau khi nhung")
    embbed_img_matrix = undomix_matrix(random_matrix,embbed_matrix)
    print_embbed_matrix_img(embbed_img_matrix,arr[:len(m)])

class Wulee():
    def __init__(self,matrixK=matrixK,matrixF=matrixF) :
        self.K = matrixK
        self.F = matrixF
        self.sumK = sum(sum(matrixK))
        self.small_matrices = self.split_matrix(matrixF)
        
    def  split_matrix(self,matrix, num_rows_small=len(matrixK), num_cols_small=len(matrixK[0])):
        num_rows_big = len(matrix)
        num_cols_big = len(matrix[0])
        
        if num_rows_big % num_rows_small != 0 or num_cols_big % num_cols_small != 0:
            print("Không thể chia ma trận thành các ma trận nhỏ với kích thước đã cho.")
            return None
        
        small_matrices = []
        for i in range(0, num_rows_big, num_rows_small):
            for j in range(0, num_cols_big, num_cols_small):
                small_matrix = [row[j:j+num_cols_small] for row in matrix[i:i+num_rows_small]]
                small_matrices.append(small_matrix)
        
        return small_matrices
    
    def hide(self,B : str):
        x = 0
        Fs = self.small_matrices
        for i in range(len(Fs)):
            if x == len(B):
                break
            print("------------------------------------")
            print(f"\nVới F{i+1}:")
            print_matrix(Fs[i])
            sumFxorK = sum(sum(np.bitwise_xor(Fs[i],self.K)))
            strF = matrix_to_array(Fs[i])
            strK = matrix_to_array(self.K)
            print(f"sum(F{i+1}^K) = {sumFxorK}, sumK = {self.sumK}")
            if sumFxorK <= 0 or sumFxorK >= self.sumK:
                print(f"sum(F{i+1}^K) = {sumFxorK} không thỏa mãn điều kiện")
                print(f"Không giấu được dữ liệu vào trong F{i+1}")
            else:
                if sumFxorK % 2 == int(B[x]):
                    print(f"sum(F{i+1}^K) = {sumFxorK} mod 2 = {B[x]} giữ nguyên F{i+1}, giấu bit {RED}{B[x]}{RESET}")
                    x +=1
                elif sumFxorK  == 1:
                    for idx in range(len(strF)):
                        if strF[idx] == 0 and strK[idx] == 1:
                            strF[idx] = 1
                            print(f"Vì sum(F{i+1}^K) = 1 nên 1 bit sẽ được giấu vào F{i+1}, giấu bit {RED}{B[x]}{RESET}")
                            newF = array_to_matrix(strF,len(self.K),len(self.K[0]))
                            print(f"New F{i+1}")
                            x += 1
                            print_embbed_matrix_img(newF,[idx+1])
                            break
                elif sumFxorK == self.sumK - 1:
                    for idx in range(len(strF)):
                        if strF[idx] == 1 and strK[idx] == 1:
                            strF[idx] = 0
                            print(f"sum(F{i+1}^K) = sumK - 1 nên 1 bit sẽ được giấu vào F{i+1}, giấu bit {RED}{B[x]}{RESET}")
                            newF = array_to_matrix(strF,len(self.K),len(self.K[0]))
                            print(f"New F{i+1}")
                            x +=1
                            print_embbed_matrix_img(newF,[idx+1])
                            break
                else:
                    for idx in range(len(strF)):
                        if strK[idx] == 1:
                            if strF[idx] == 0:
                                strF[idx] = 1
                            else:
                                strF[idx] = 0
                            print(f"sum(F{i+1}^K) = {sumFxorK} thỏa mãn DK nên 1 bit sẽ được giấu vào F{i+1}, giấu bit {RED}{B[x]}{RESET}")
                            newF = array_to_matrix(strF,len(self.K),len(self.K[0]))
                            x += 1
                            print(f"New F{i+1}")
                            print_embbed_matrix_img(newF,[idx+1])
                            break
                
        
                
# Example usage:
# matrix = np.array([
#     [231, 32, 233, 161, 24, 71, 140, 245],
#     [247, 40, 248, 245, 124, 204, 36, 107],
#     [234, 202, 245, 167, 9, 217, 239, 173],
#     [193, 190, 100, 167, 43, 180, 8, 70],
#     [11, 24, 210, 177, 81, 243, 8, 112],
#     [97, 195, 203, 47, 125, 114, 165, 181],
#     [193, 70, 174, 167, 41, 30, 127, 245],
#     [87, 149, 57, 192, 65, 129, 178, 228]
# ])

