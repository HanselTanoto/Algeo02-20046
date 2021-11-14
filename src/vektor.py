import numpy as np

def eigen(M):
# Menghitung vektor dan nilai eigen dengan algoritma simultaneous power iteration
    m, n = M.shape
    # mengisi Q dengan nilai random
    Q = np.random.rand(m,m)
    # Dekomposisi QR
    Q, R = np.linalg.qr(Q)
    prevQ = Q
    # Iterasi hingga error cukup kecil
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
