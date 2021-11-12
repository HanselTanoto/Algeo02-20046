import numpy as np
def simultaneous_power_iteration(A):
    n, m = A.shape
    Q = np.random.rand(n,1000)
    Q, _ = np.linalg.qr(Q)
    Q_prev = Q
 
    for i in range(1000):
        Z = A.dot(Q)
        Q, R = np.linalg.qr(Z)
        
        err = ((Q - Q_prev) ** 2).sum()
        if i % 10 == 0:
            print(i, err)

        Q_prev = Q
        if err < 1e-3:
            break

    return np.diag(R), Q

A = np.array([[3,0],[8,-1]])
nilai_eigen,vektor_eigen = simultaneous_power_iteration(A)
print(nilai_eigen)
print(vektor_eigen)