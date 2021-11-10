import timeit
import cv2
from PIL import Image
import numpy as np
import vektor           # fungsi/prosedur menghitung nilai dan vektor eigen (vektor.py)
import svd              # fungsi/prosedur menghitung svd (svd.py)

# Timer Start
start = timeit.default_timer()

# Open image
image = Image.open(r"test\Coffee.jpg")
M = np.asarray(image).astype(float)       # convert image to matrix
print(M)
M_b, M_g, M_r = cv2.split(M)              # split matriks ke matriks RGB

compress = int(input("Skala kompresi (%): "))

# matriks U, S, V_T masing masing warna (RGB)
Ub, Sb, V_Tb = svd.matrixSVD(M_b)
Ug, Sg, V_Tg = svd.matrixSVD(M_g)
Ur, Sr, V_Tr = svd.matrixSVD(M_r)

# mengambil hanya mxk matriks U, kxk S, dan kxn matriks V_T
nUb, nSb, nV_Tb = svd.compress(M_b, Ub, Sb, V_Tb, compress)
nUg, nSg, nV_Tg = svd.compress(M_g, Ug, Sg, V_Tg, compress)
nUr, nSr, nV_Tr = svd.compress(M_r, Ur, Sr, V_Tr, compress)

# membentuk matriks kembali dari U, S, V_T
new_Mb = svd.multiplySVD(nUb, nSb, nV_Tb)
new_Mg = svd.multiplySVD(nUg, nSg, nV_Tg)
new_Mr = svd.multiplySVD(nUr, nSr, nV_Tr)

# menggabungkan matriks RGB
new_M = cv2.merge([new_Mb, new_Mg, new_Mr])
new_M = np.clip(new_M, 0, 255)
print(new_M)
# convert matriks RGB ke image
img = Image.fromarray(new_M.astype(np.uint8), 'RGB')
img.save('test\Test.jpg')
img.show()

# Timer Stop
stop = timeit.default_timer()
print('Time: ', stop - start)  