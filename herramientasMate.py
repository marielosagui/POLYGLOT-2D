import numpy as np

def PrimeroCero(M, n):
    for i in range(n):
        row = [0.0]*n
        M.append(row)

def SegundoCero(M, n, m):
    for i in range(n):
        row = [0.0]*m 
        M.append(row)

def TercerCero(v, n):
    for i in range(n):
        v.append(0.0)

def copyMatrix(A, copy):
    PrimeroCero(copy,len(A))
    for i in range(len(A)):
        for j in range(len(A)):
            copy[i][j] = A[i][j]

def calculateMember(i, j, r, A, B):
    member = 0
    for k in range (r):
        member += A[i][k] * B[k][j]
    return member

def productoMxV(A, v, R):
    for f in range(len(A)):
        cell = 0.0
        for c in range(len(v)):
            cell += A[f][c] * v[c]
    R[f] += cell
    
def productoMxM(A, B, n, r, m):
    R = []
    SegundoCero(R, n , m)
    for i in range(n):
        for j in range(m):
            R[i][j] = calculateMember(i, j, r, A, B)
    return R



def productoRMatrix(real, M, R):
    PrimeroCero(R, len(M))
    for i in range(len(M)):
        for j in range(len(M[0])):
            R[i][j] = real * M[i][j]

def menorm( M, i, j):
    del M[i]
    for i in range(len(M)):
        del M[i][j]

def determinantem(M):
    if len(M) == 1 : return M[0][0]
    else:
        det = 0.0
        for i in range(len(M[0])):
            minor = []
            copyMatrix(M, minor)
            menorm(minor, 0, i)
            det +=  pow(-1, i) * M[0][i] * determinantem(minor)
        return det

def mcofactores(M, Cof):
    PrimeroCero(Cof, len(M))
    for i in range(len(M)):
        for j in range(len(M[0])):
            minor = []
            copyMatrix(M, minor)
            menorm(minor, i, j)
            Cof[i][j] = pow(-1, i+j) * determinantem(minor)

def transpuesta(M, T):
    SegundoCero(T,len(M[0]), len(M))
    for i in range(len(M)):
        for j in range(len(M[0])):
            T[j][i]  = M[i][j]

def Minversa(M, Minv):
    print("Iniciando calculo de inversa...\n")
    Cof = []
    Adj = []
    print("Calculo de determinante...\n")
    det = determinantem(M)
    if det == 0 : exit()
    print("Iniciando calculo de cofactores...\n")
    mcofactores(M,Cof)
    print("Calculo de adjunta...\n")
    transpuesta(Cof,Adj)
    print("Calculo de inversa...\n")
    productoRMatrix(1/det, Adj, Minv)