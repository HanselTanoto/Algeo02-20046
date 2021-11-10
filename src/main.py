import timeit
import cv2
from PIL import Image
import numpy as np
import vektor           # fungsi/prosedur menghitung nilai dan vektor eigen (vektor.py)
import svd              # fungsi/prosedur menghitung svd (svd.py)

# Timer Start
start = timeit.default_timer()

# Open image
image = Image.open(r"Test Image\Coffee.jpg")
M = np.asarray(image).astype(float)       # convert image to matrix
print(M)
M_b, M_g, M_r = cv2.split(M)              # split matriks ke matriks RGB

compress = int(input("Skala kompresi (%): "))

# matriks U, S, V_T masing masing warna (RGB)
Ub, Sb, V_Tb = svd(M_b, compress)
Ug, Sg, V_Tg = svd(M_g, compress)
Ur, Sr, V_Tr = svd(M_r, compress)

# membentuk matriks kembali dari U, S, V_T
new_Mb = svd.multiplySVD(Ub, Sb, V_Tb)
new_Mg = svd.multiplySVD(Ug, Sg, V_Tg)
new_Mr = svd.multiplySVD(Ur, Sr, V_Tr)

# menggabungkan matriks RGB
new_M = cv2.merge([new_Mb, new_Mg, new_Mr])
print(new_M)
# convert matriks RGB ke image
img = Image.fromarray(new_M.astype(np.uint8), 'RGB')
img.save('Test Image/Test.jpg')
img.show()

# Timer Stop
stop = timeit.default_timer()
print('Time: ', stop - start)  