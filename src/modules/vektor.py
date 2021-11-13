import numpy as np

def eigen(M):
# Menghitung vektor dan nilai eigen
    m, n = M.shape
    Q = np.random.rand(m,m)
    # Dekomposisi QR
    Q, R = np.linalg.qr(Q)
    prevQ = Q
    # Iterasi hingga error kecil
    for i in range(200):
        Temp = np.dot(M,Q)
        Q, R = np.linalg.qr(Temp)
        error = ((Q - prevQ) ** 2).sum()
        prevQ = Q
        if error < 0.001:
            break
    e_val = np.diag(R)
    e_vec = Q
    return e_val, e_vec
