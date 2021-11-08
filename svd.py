import numpy as np
from PIL import Image
import timeit
import cv2

# Timer Start
start = timeit.default_timer()

# convert image to array
image = Image.open(r"Test Image\Chrome_Logo.jpg")
Arr = np.array(image)
print(Arr)
m,n,c = Arr.shape
print(m,n,c)    # dimensi array : (panjang,lebar,dimensi_warna) 
# split array to r g b array
Arr_b, Arr_g, Arr_r = cv2.split(Arr)
print(Arr_b)
print(Arr_g)
print(Arr_r)
# transpose dari r, g, b array
Arr_b_T = np.transpose(Arr_b)
Arr_g_T = np.transpose(Arr_g)
Arr_r_T = np.transpose(Arr_r)
# hitung transpose(A).A untuk cari matriks V dan Sigma
Arr_T_Arr_b = np.dot(Arr_b_T,Arr_b)
Arr_T_Arr_g = np.dot(Arr_g_T,Arr_g)
Arr_T_Arr_r = np.dot(Arr_r_T,Arr_r)
# hitung A.transpose(A) untuk cari matriks U
Arr_Arr_T_b = np.dot(Arr_b,Arr_b_T)
Arr_Arr_T_g = np.dot(Arr_g,Arr_g_T)
Arr_Arr_T_r = np.dot(Arr_r,Arr_r_T)

# compression rate
compress = 100
new_m = int(compress/100*m)
new_n = int(compress/100*n)

# hitung eigen value dan eigen vector matriks blue, untuk sementara (testing)
w,v = np.linalg.eig(Arr_Arr_T_b)
w = np.flip(w, axis=0)
v = np.flip(v, axis=1)
print('E-value:', w)
print('E-vector', v)

# Matriks U (Singular kiri)
U = np.zeros((m,new_m))
print(U.shape)
for i in range(m):
    for j in range(new_m):
        U[i][j] = v[i][j]
print(U)

# Matriks Sigma
S = np.zeros((new_m,new_n))
k = min(new_m,new_n)
print(S.shape)
for i in range(k):
    for j in range(k):
        S[i][j] = w[i]

# hitung eigen value dan eigen vector matriks blue, untuk sementara (testing)
w,v = np.linalg.eig(Arr_T_Arr_b)
w = np.flip(w, axis=0)
v = np.flip(v, axis=1)
print('E-value:', w)
print('E-vector', v)
v_T = np.transpose(v)

# Matriks V (Singular kanan)
V = np.zeros((new_n,n))
for i in range(new_n):
    for j in range(n):
        V[i][j] = v_T[i][j]

new_matrix = np.dot(U,S)
new_matrix = np.dot(new_matrix,V)

img = Image.fromarray(new_matrix, 'L')
img.save('Test Image/Test.jpg')
img.show()

"""
for i in range(n):
    norm = np.linalg.norm(v[i])
    V[i] = v[i]/norm
print(V)
"""

"""
A = np.array([[3,4,3],[1,2,3],[4,2,1],[3,2,4]])
row = A.shape[0]
A2 = [[0 for j in range (4)] for i in range (3)]
# convert array ke image lagi, keterangan: 'L' untuk grayscale, 'RGB' untuk berwarna
img = Image.fromarray(r, 'L')
img.save('Test.jpg')
img.show()

A = np.array([[10,0,2],[0,10,4],[2,4,2]])
w,v = np.linalg.eig(A)
print('E-value:', w)
print('E-vector', v)
w = np.flip(w, axis=0)
v = np.flip(v, axis=1)
print('E-value:', w)
print('E-vector', v)
"""

# Timer Stop
stop = timeit.default_timer()
print('Time: ', stop - start)  
