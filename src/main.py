import timeit
from PIL import Image
import numpy as np
import vektor           # fungsi/prosedur menghitung nilai dan vektor eigen (vektor.py)
import svd              # fungsi/prosedur menghitung svd (svd.py)

# Timer Start
start = timeit.default_timer()

# Open image
file_name = "Tiger_BW.jpg"
img = Image.open(r"test\\"+file_name)
M = np.asarray(img).astype(float)       # convert image to matrix

# skala kompresi
c_rate = int(input("Skala kompresi (%): "))

# jenis gambar : color/grayscale
if (M.ndim == 2):
    new_M, size0, new_size = svd.svdGrayscale(M, c_rate)
    c_img = Image.fromarray(new_M.astype(np.uint8), 'L')
elif (M.ndim == 3):
    new_M, size0, new_size = svd.svdColor(M, c_rate)
    c_img = Image.fromarray(new_M.astype(np.uint8), 'RGB')

# ukuran awal dan setelah dikompresi
print("Initial size:", size0, "bytes")
print("Compressed size:", new_size, "bytes")

# save image
c_img.save('test\\'+'compressed'+str(c_rate)+"_"+file_name)
c_img.show()

# Timer Stop
stop = timeit.default_timer()
print('Time: ', stop - start)  