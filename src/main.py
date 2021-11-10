import timeit
import cv2
from PIL import Image
import numpy as np
import vektor           # fungsi/prosedur menghitung nilai dan vektor eigen (vektor.py)
import svd              # fungsi/prosedur menghitung svd (svd.py)

# Timer Start
start = timeit.default_timer()

# Open image
image = Image.open(r"test\Chrome_Logo.jpg")
M = np.asarray(image).astype(float)       # convert image to matrix
M_b, M_g, M_r = cv2.split(M)              # split matriks ke matriks R,G,B
m,n,c = M.shape

# ukuran awal
size0 = m * n * 3
print("Initial size:", size0, "bytes")

compress = int(input("Skala kompresi (%): "))

# matriks U, S, V_T masing masing warna (RGB)
Ub, Sb, V_Tb = svd.matrixSVD(M_b)
Ug, Sg, V_Tg = svd.matrixSVD(M_g)
Ur, Sr, V_Tr = svd.matrixSVD(M_r)

# mengambil hanya mxk matriks U, kxk S, dan kxn matriks V_T
nUb, nSb, nV_Tb, sizeb = svd.compress(Ub, Sb, V_Tb, compress)
nUg, nSg, nV_Tg, sizeg = svd.compress(Ug, Sg, V_Tg, compress)
nUr, nSr, nV_Tr, sizer = svd.compress(Ur, Sr, V_Tr, compress)
size = sizeb + sizeg + sizer

# membentuk matriks kembali dari U, S, V_T
new_Mb = svd.multiplySVD(nUb, nSb, nV_Tb)
new_Mg = svd.multiplySVD(nUg, nSg, nV_Tg)
new_Mr = svd.multiplySVD(nUr, nSr, nV_Tr)

# menggabungkan matriks R,G,B
new_M = cv2.merge([new_Mb, new_Mg, new_Mr])
new_M = np.clip(new_M, 0, 255)
# convert matriks RGB ke image
img = Image.fromarray(new_M.astype(np.uint8), 'RGB')
img.save('test\Test.jpg')
img.show()

# ukuran setelah dikompresi
print("Compressed size:", size, "bytes")

# Timer Stop
stop = timeit.default_timer()
print('Time: ', stop - start)  