import numpy as np

Al = np.array([[1, 0, -1, 0, 0, 2, 0, 1], [0, 0, 1, 0, 3, 0, 0, 1], [1, 0, 0, 0, 1, 0, 0, 0], [0, 5, 0, 1, 0, 0, 0, -2],
               [0, 0, 0, 1, 0, 0, 0, 0], [0, 0, -2, -1, -1, 0, 0, 0], [1, 0, 0, 0, 0, 1, 0, 0]])

B = np.random.rand(8, 8)

C = np.dot(Al, B)

(rows, cols) = Al.nonzero()
(m, n) = Al.shape
(p, q) = B.shape

AB = np.zeros((m, q))

for i in range(m):
    for j in range(q):
        for k in range(n):
            if i in rows and k in cols:
                AB[i, j] += Al[i][k] * B[k][j]

print(np.allclose(np.dot(Al, B), AB))

# -------------------------------------------------
# Compressão de linhas esparsas (CSR, CRS ou Formato Yale);

A = []
JA = []
Counter = []
for i in range(m):
    c = 0
    colum = 0
    for a in Al[i, :]:
        colum += 1
        if a != 0:
            c = c + 1
            A.append(a)
            JA.append(colum)
        else:
            pass
    Counter.append(c)
A = np.array(A)
JA = np.array(JA)
JA = JA - 1

IA = [0]
for i in range(1, m + 1):
    IA.append(IA[i - 1] + Counter[i - 1])