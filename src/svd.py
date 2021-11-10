import math
import numpy as np


def svd(M, compress):
# Menghitung nilai Matriks U, S, dan V_T dari matriks M dengan skala kompresi (compress)
    M_T = np.transpose(M)       # transpose(M)
    M_M_T = np.dot(M, M_T)      # M*transpose(M)
    M_T_M = np.dot(M_T, M)      # transpose(M)*M
    m, n = M.shape              # dimensi M
    dim = min(m,n)
    k = int(compress/100*dim)   # faktor kompresi
    
    # Matriks U
    e_val1, e_vec1 = np.linalg.eigh(M_M_T)
    e_val1 = np.flip(e_val1, axis=0)
    e_vec1 = np.flip(e_vec1, axis=0)
    U = np.zeros((m,k))
    for i in range(m):
        for j in range(k):
            U[i][j] = e_vec1[i][j]
    
    # Matriks Sigma
    e_val2, e_vec2 = np.linalg.eigh(M_T_M)
    e_val2 = np.flip(e_val2, axis=0)
    e_vec2 = np.flip(e_vec2, axis=0)
    S = np.zeros((k,k))
    for i in range(k):
        S[i][i] = math.sqrt(e_val2[i])
    
    # Matriks V_T
    e_vec1_i = np.linalg.inv(e_vec1)
    # Cari matriks U invers
    U_i = np.zeros((k,m))
    for i in range(k):
        for j in range(m):
            U_i[i][j] = e_vec1_i[i][j]
    # Cari matriks S invers
    S_i = np.linalg.inv(S)
    # Hitung V_T = S_i*V_i*M
    V_T = np.dot(U_i,M)
    V_T = np.dot(S_i,V_T)

    # Dimensi U, S, V_T
    print(U.shape)
    print(S.shape)
    print(V_T.shape)
    return U, S, V_T


def multiplySVD(U, S, V_T):
# Menghitung hasil perkalian matriks U, S, dan V_T 
    result = np.dot(U,S)
    result = np.dot(result,V_T)
    return result