import numpy as np


def Kronecker_direto(A, B):
    A = np.array(A)
    B = np.array(B)
    (m, n) = A.shape
    (p, q) = B.shape

    K = np.zeros((m * p, n * q))

    for i in range(m):
        for j in range(n):
            K[i * p:(i + 1) * p, j * q:(j + 1) * q] = A[i, j] * B

    return K

#
# # Testes
# A = [[1, 2, 3], [4, 5, 6]]
# B = [[1, 2, 3, 4], [5, 6, 7, 8]]
#
# print(Kronecker_direto(A, B))

with open('C:\\Users\\viniv\\Desktop\\LB comp\\A.txt') as arquivo:
    Dados = arquivo.readlines()

Dados.remove(Dados[1001])
Dados.remove(Dados[1000])

matriz = []
for linha in Dados:
    matriz.append(linha.rstrip('\n').lstrip(' ').split(' '))

matriz = np.array(matriz, dtype='float')

with open('C:\\Users\\viniv\\Desktop\\LB comp\\B.txt') as arquivo1:
    Dados1 = arquivo1.readlines()

Dados1.remove(Dados1[1507])
Dados1.remove(Dados1[1506])
Dados1.remove(Dados1[1505])
Dados1.remove(Dados1[1504])

matriz1 = []
for linha in Dados1:
    matriz1.append(linha.rstrip('\n').lstrip(' ').split())

M = []
for linha in matriz1:
    n = len(linha)
    if n == 600:
        M.append(linha)
M = np.array(M, dtype='float')

A = np.array(matriz)
B = np.array(M)
(m, n) = A.shape
(p, q) = B.shape

with open('C:\\Users\\viniv\\Desktop\\LB comp\\Kronecker.txt', 'a') as Kron:
    for j in range(n):
        for i in range(m):
            if i == j:
                print('Next {}'.format(i))
            st = A[i, j] * B
            Kron.write(format(st))
            Kron.write('\n')
        Kron.write('Fim da primeira coluna')
        Kron.write('\n')
