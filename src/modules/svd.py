import numpy as np
import cv2
import vektor           # untuk cari nilai dan vektor eigen

def matrixSVD(M):
# mendekomposisi M menjadi U, s, dan V_T
    M_T = np.transpose(M)       # transpose(M)
    M_M_T = np.dot(M, M_T)      # M*transpose(M)
    M_T_M = np.dot(M_T, M)      # transpose(M)*M
 
    # hitung vektor dan nilai eigen
    e_val, e_vec = vektor.eigen(M_M_T)
    e_val = np.sort(e_val)[::-1]
    
    U = e_vec                  # Matriks U / Singular kiri 
    s = np.sqrt(e_val)         # Nilai singular

    # Matriks V_T / Singular kanan
    U_i = np.linalg.inv(U)                      # Cari matriks U invers
    s_i = 1/s                                   # Cari matriks S invers
    S_i = np.zeros((M.shape[1], M.shape[0]))
    x = min(M.shape[1], M.shape[0])
    S_i[:x, :x] = np.diag(s_i[:x])
    V_T = np.dot(S_i,np.dot(U_i,M))             # Hitung V_T = S_i*V_i*M

    return U, s, V_T


def compress(U, s, V_T, rate):
# mengambil hanya mxk matriks U, kxk S, dan kxn matriks V_T
    m,n = U.shape[0], V_T.shape[0]      # dimensi 
    k = int((rate*(m*n)/100)/(m+n+1))   # faktor skala kompresi
    nU = U[:, 0:k]                      # ambil mxk matriks U
    ns = s[0:k]                         # ambil k data pertama dari s (nilai singular)
    nV_T = V_T[0:k, :]                  # ambil kxn matriks V_T
    size =  m*k + k + k*n
    return nU, ns, nV_T, size


def multiplySVD(nU, ns, nV_T):
# Menghitung hasil perkalian matriks U, S, dan V_T 
    result = np.dot(np.dot(nU,np.diag(ns)),nV_T)
    return result


def svdCompression(M, c_rate):
# kompresi matriks gambar dengan svd
    U, S, V_T = matrixSVD(M)
    nU, nS, nV_T, size = compress(U, S, V_T, c_rate)
    new_M = multiplySVD(nU, nS, nV_T)
    return new_M, size


def svdColor(M, c_rate):
    # ukuran awal
    m,n,c = M.shape
    size0 = (m * n) * c
    # split matriks ke matriks R,G,B
    M_b, M_g, M_r = cv2.split(M)
    # svd compression
    new_M_b, size_b = svdCompression(M_b, c_rate)
    new_M_g, size_g = svdCompression(M_g, c_rate)
    new_M_r, size_r = svdCompression(M_r, c_rate)
    new_size = size_b + size_g + size_r
    # menggabungkan matriks R,G,B
    new_M = cv2.merge([new_M_b, new_M_g, new_M_r])
    new_M = np.clip(new_M, 0, 255)
    return new_M, size0, new_size


def svdGrayscale(M, c_rate):
    # ukuran awal
    m, n = M.shape
    size0 = m * n
    # svd compression
    new_M, new_size = svdCompression(M, c_rate)
    new_M = np.clip(new_M, 0, 255)
    return new_M, size0, new_size


def svdColorPNG(M, c_rate):
    # ukuran awal
    m,n,c = M.shape
    size0 = (m * n) * c
    # split matriks ke matriks R,G,B,A
    M_b, M_g, M_r, M_a = cv2.split(M)
    # svd compression
    new_M_b, size_b = svdCompression(M_b, c_rate)
    new_M_g, size_g = svdCompression(M_g, c_rate)
    new_M_r, size_r = svdCompression(M_r, c_rate)
    new_M_a, size_a = svdCompression(M_a, c_rate)
    new_size = size_b + size_g + size_r + size_a
    # menggabungkan matriks R,G,B,A
    new_M = cv2.merge([new_M_b, new_M_g, new_M_r, new_M_a])
    new_M = np.clip(new_M, 0, 255)
    return new_M, size0, new_size