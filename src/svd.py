import numpy as np
import vektor           # untuk cari nilai dan vektor eigen

def matrixSVD(M):
# mendekomposisi M menjadi U, s, dan V_T
    M_T = np.transpose(M)       # transpose(M)
    M_M_T = np.dot(M, M_T)      # M*transpose(M)
    M_T_M = np.dot(M_T, M)      # transpose(M)*M
    
    e_val1, e_vec1 = np.linalg.eigh(M_M_T)      # sementara
    e_val1 = np.flip(e_val1, axis=0)            # 
    e_vec1 = np.flip(e_vec1, axis=1)            # 
    U = e_vec1                  # Matriks U / Singular kiri 
    s = np.sqrt(e_val1)         # Nilai singular

    # Matriks V_T / Singular kanan
    U_i = np.linalg.inv(U)                      # Cari matriks U invers
    s_i = 1/s                                   # Cari matriks S invers
    S_i = np.zeros((M.shape[1], M.shape[0]))
    S_i[:M.shape[0], :M.shape[0]] = np.diag(s_i)
    V_T = np.dot(S_i,np.dot(U_i,M))             # Hitung V_T = S_i*V_i*M

    return U, s, V_T


def compress(U, s, V_T, rate):
# mengambil hanya mxk matriks U, kxk S, dan kxn matriks V_T
    m,n = U.shape[0], V_T.shape[0]      # dimensi 
    k = int(rate/100*min(m,n))          # faktor skala kompresi
    nU = U[:, 0:k]                      # ambil mxk matriks U
    ns = s[0:k]                         # ambil k data pertama dari s (nilai singular)
    nV_T = V_T[0:k, :]                  # ambil kxn matriks V_T
    size =  m*k + k + k*n
    return nU, ns, nV_T, size


def multiplySVD(nU, ns, nV_T):
# Menghitung hasil perkalian matriks U, S, dan V_T 
    result = np.dot(np.dot(nU,np.diag(ns)),nV_T)
    return result