# vektor eigen
baris = 10
kolom = 10
matriks = [[0 for j in range(baris)] for i in range(kolom)]

def determinan(matriks,barismatriks, kolommatriks):
    matriksdet = [[0 for j in range(kolommatriks)] for i in range(barismatriks)]
    det = 1
    # copy matriks
    for i in range(barismatriks):
        for j in range(kolommatriks):
            matriksdet[i][j] = matriks[i][j]
    for i in range(1,barismatriks):
        for j in range(kolommatriks):
            obe = float(matriksdet[i][j])/float(matriksdet[j][j])
            for k in range(kolommatriks):
                matriksdet[i][k] -= obe * matriksdet[j][k] 
    for i in range(barismatriks):
        for j in range(kolommatriks):
            if(i == j):
                det *= matriksdet[i][j]
    if det == 0 or det == -0:
        det = 0
    return det

matriksidentitas = [[0 for j in range(baris)] for i in range(kolom)]
for i in range(baris):
    for j in range(kolom):
        if (i == j):
            matriksidentitas[i][j] = 1

eigen = [0 for i in range(baris)]