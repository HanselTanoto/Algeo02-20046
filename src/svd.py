import numpy as np
import vektor

def matrixSVD(M):
    M_T = np.transpose(M)       # transpose(M)
    M_M_T = np.dot(M, M_T)      # M*transpose(M)
    M_T_M = np.dot(M_T, M)      # transpose(M)*M
    
    # Matriks U
    e_val1, e_vec1 = np.linalg.eigh(M_M_T)
    e_val1 = np.flip(e_val1, axis=0)
    e_vec1 = np.flip(e_vec1, axis=0)
    U = e_vec1

    # Matriks Sigma
    e_val2, e_vec2 = np.linalg.eigh(M_T_M)
    e_val2 = np.flip(e_val2, axis=0)
    e_vec2 = np.flip(e_vec2, axis=0)
    S = np.sqrt(e_val2)

    # Matriks V_T
    U_i = np.linalg.inv(U)                      # Cari matriks U invers
    S_i = 1/S                                   # Cari matriks S invers
    V_T = np.dot(np.diag(S_i),np.dot(U_i,M))    # Hitung V_T = S_i*V_i*M

    # Dimensi U, S, V_T
    print(U.shape)
    print(S.shape)
    print(V_T.shape)

    return U, S, V_T


def compress(M, U, S, V_T, rate):
# mengambil hanya mxk matriks U, kxk S, dan kxn matriks V_T
    m,n = M.shape
    k = int(rate/100*max(m,n))
    nU = U[:, 0:k]
    nS = S[0:k]
    nV_T = V_T[0:k, :]
    return nU, nS, nV_T


def multiplySVD(nU, nS, nV_T):
# Menghitung hasil perkalian matriks U, S, dan V_T 
    result = np.dot(np.dot(nU,np.diag(nS)),nV_T)
    return result