from total import *
from matrix import *
from gg import *
# Example usage:
def test_random_hide_and_seek():
    a = 19
    p = 37
    m = "00011011"
    matrix = matrix66
    random_hide_and_seek(matrix,m,a,p)
def test_wulee():
    wl = Wulee()
    B="011"
    wl.hide(B)

def test_sequence_hide_and_seek():
    matrix = matrix44
    m= "01011101"
    sequence_hide_and_seek(matrix,m)
    
# test_sequence_hide_and_seek()

def test_jsteg():
    matrix = matrixJsteg
    m="01101011"
    jteg = Jsteg()
    jteg.hide(matrix,m)

og = Outguess(matrixJsteg)   
matrix = matrixJsteg
arr = og.zigzag(matrix)
mt1 = array_to_matrix(arr,len(matrix),len(matrix[0]))
mt2 = og.shift_k_bit(3,mt1)
m="01101011"
og.hide(mt2,m)