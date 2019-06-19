import numpy as np
import time

# Aula 14/05/2019:

# Exemplo.: Construir uma função que recebe um número e retorna esse número ao quadrado.


def square(x):
    return x ** 2 - np.pi


# Método da bissecção:

def bissec(a, b, f, TOL=1e-10):
    if b - a < 0:
        print('Erro!')

    if np.abs(f(a)) < TOL:
        print('Congratulations you have found a root of the function ! X = {}'.format(a))
        return a
    elif np.abs(f(b)) < TOL:
        print('Congratulations you have found a root of the function ! X = {}'.format(b))
        return b

    elif f(a) * f(b) > 0:
        return print('Ops!')

    Xo = (a + b) / 2
    iter = 0
    while np.abs(f(Xo)) > TOL:

        if f(Xo) * f(a) > 0:
            a = Xo
        else:
            b = Xo

        Xo = (a + b) / 2
        iter += 1

    print('Congratulations you have found a root of function ! X = {} after {} iterations.'.format(Xo, iter))
    return Xo


print(bissec(0, 3, square, 1e-12))

def counter(n):

    def fatorial(n):
        fat = 1
        for k in range(n, 0, -1):
            fat *= k

        return fat


    def fatr(n):
        if n == 0 or n == 1:
            return 1
        else:
            n *= fatr(n - 1)
        return n

    t1 = time.time()
    p = fatorial(n)
    t1f = time.time() - t1
    print(t1f)

    t2 = time.time()
    fatr(n)
    t2f = time.time() - t2
    print(t2f)

    return p
