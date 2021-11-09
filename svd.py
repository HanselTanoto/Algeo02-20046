import math
import numpy as np
from PIL import Image
import timeit
import cv2

# Timer Start
start = timeit.default_timer()

import math
import numpy as np
from PIL import Image
import timeit
import cv2

def svd(A, k):
    A_T = np.transpose(A)
    A_A_T = np.dot(A, A_T)
    A_T_A = np.dot(A_T, A)
    m, n = A.shape
    new_m = int(k/100*m)
    new_n = int(k/100*n)
    # Matriks U
    e_val1, e_vec1 = np.linalg.eigh(A_A_T)
    e_val1 = np.flip(e_val1, axis=0)
    e_vec1 = np.flip(e_vec1, axis=0)
    U = np.zeros((m,new_m))
    for i in range(m):
        for j in range(new_m):
            U[i][j] = e_vec1[i][j]
    # Matriks V dan Sigma
    e_val2, e_vec2 = np.linalg.eigh(A_T_A)
    e_val2 = np.flip(e_val2, axis=0)
    e_vec2 = np.flip(e_vec2, axis=0)
    """
    V = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            V[i][j] = e_vec2[i][j]
    V_T = np.transpose(V)
    """
    k = min(new_m,new_n)
    S = np.zeros((new_m,new_n))
    for i in range(k):
        S[i][i] = math.sqrt(e_val2[i])
    e_vec1_i = np.linalg.inv(e_vec1)
    U_i = np.zeros((new_m,m))
    for i in range(new_m):
        for j in range(m):
            U_i[i][j] = e_vec1_i[i][j]
    S_i = np.zeros((new_n,new_m))
    for i in range(k):
        S_i[i][i] = 1/math.sqrt(e_val2[i])
    V_T = np.dot(U_i,A)
    V_T = np.dot(S_i,V_T)
    print(U.shape)
    print(S.shape)
    print(V_T.shape)
    return U, S, V_T


image = Image.open(r"Test Image\Coffee.jpg")
Arr = np.asarray(image).astype(float)
print(Arr)

Arr_b, Arr_g, Arr_r = cv2.split(Arr)

k = 99

Ub, Sb, V_Tb = svd(Arr_b, k)
Ug, Sg, V_Tg = svd(Arr_g, k)
Ur, Sr, V_Tr = svd(Arr_r, k)

new_matrix1 = np.dot(Ub,Sb)
new_matrix1 = np.dot(new_matrix1,V_Tb)
new_matrix2 = np.dot(Ug,Sg)
new_matrix2 = np.dot(new_matrix2,V_Tg)
new_matrix3 = np.dot(Ur,Sr)
new_matrix3 = np.dot(new_matrix3,V_Tr)

new_matrix = cv2.merge([new_matrix1, new_matrix2, new_matrix3])
print(new_matrix)

img = Image.fromarray(new_matrix.astype(np.uint8), 'RGB')
img.save('Test Image/Test.jpg')
img.show()

# Timer Stop
stop = timeit.default_timer()
print('Time: ', stop - start)  
