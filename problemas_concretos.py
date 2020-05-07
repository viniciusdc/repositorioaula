import numpy as np
import matplotlib.pyplot as plt
import time


# Diferenças finitas:

# Exemplo:
def sen(x):
    return np.sin(x)


'Problema calcular o valor de Df para x in [0, pi] aproximar. '


def d_sen(x, n):
    h = np.pi / n
    return (sen(x + h) - sen(x)) / h


# -----------------------------------------------------------------------
# Método de Euler:

# Solução para o problema y' = y, com y'(t) = x.


# Condições de valor inicial:
# Ponto incial:
to = 0
# Valor incial:
yo = 1

b = 10
n = 1000

h = int(abs(b - to)) / n

x = np.linspace(to, b, n + 1)

F = np.zeros(n + 1)
F[0] = yo

for i in range(1, n + 1):
    F[i] = (h + 1) * F[i - 1]
# Plot solução real:

plt.plot(x, np.exp(x))
# Plot solução aprox.
plt.plot(x, F)

plt.show()

# ---------------------------------------------------------------------------
# Método de Monte Carlo.

# Pontos sorteados:
m = 10000
# Verificação dos pontos

Circulo = 0.0
to = time.time()
for k in range(m):
    x = np.random.rand() * 2
    y = np.random.rand() * 2
    if (x - 1) ** 2 + (y - 1) ** 2 <= 1:
        Circulo += 1
t = time.time() - to
pi = 4 * (Circulo / m)
Erro = abs(np.pi - pi)
# print('Valor aprox. : {}, Valor de Erro: {} e tempo de execução: {}'.format(pi, Erro, t))


def f(x, y):
    return x ** 2 + y ** 2
