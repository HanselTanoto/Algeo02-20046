import timeit
from PIL import Image
import numpy as np
import vektor           # fungsi/prosedur menghitung nilai dan vektor eigen (vektor.py)
import svd              # fungsi/prosedur menghitung svd (svd.py)

def main(file_name, c_rate):
    # Timer Start
    start = timeit.default_timer()

    # Open image
    img = Image.open(r"static\uploads\\"+file_name)
    M = np.asarray(img).astype(float)       # convert image to matrix

    # jenis gambar : color/grayscale/png
    if (M.ndim == 2):
        new_M, size0, new_size = svd.svdGrayscale(M, c_rate)
        c_img = Image.fromarray(new_M.astype(np.uint8), 'L')
    elif (M.ndim == 3 and M.shape[2] == 3):
        new_M, size0, new_size = svd.svdColor(M, c_rate)
        c_img = Image.fromarray(new_M.astype(np.uint8), 'RGB')
    elif (M.ndim == 3 and M.shape[2] == 4):
        new_M, size0, new_size = svd.svdColorPNG(M, c_rate)
        c_img = Image.fromarray(new_M.astype(np.uint8), 'RGBA')

    # Timer Stop
    stop = timeit.default_timer()
    Time = round(stop - start, 3)

    # Ouput
    init_size   = 'Initial Size     : ' + str(size0) + ' bytes'
    comp_size   = 'Compressed Size  : ' + str(new_size) + ' bytes'  
    percentage  = 'Image Pixel Difference Percentage    : ' + str(round(float(new_size/size0*100), 2)) + '%'  
    time        = 'Image Compression Time   : ' + str(Time) + ' seconds'  
    return init_size, comp_size, percentage, time, c_img