# _*_ coding: utf-8 _*_

# Atividade:

def j():
    tempo = float(input('Entre com o tempo de capitalização: '))
    i = 0.12
    Ci = 2000

    # Juros simples:
    Montante_simples = Ci * i * tempo
    Montante_composto = Ci * ((1 + i) ** tempo)

    print('Os respectivos montantes são: {} e {}'.format(Montante_simples, Montante_composto))


j()

# tarefas : Spider

# Aula 2

# Vamos trabalhar com o uso de listas.

alunos = ['leonardo', 'léo', 'vinícius', 'marcello', 'luíz guilherme', 'francisco']
alunos.sort()
alunos.append('melissa')


def oscar():
    Oscar = ['Black Panther', 'BlacKkKlansman', 'Bohemian Rhapsody',
             'The Favourite', 'Green Book', 'Roma', 'A Star Is Born', 'Vice']
    choice = input('Deseja adicionar algum item à lista ? Responda s para sim ou n para não. ')
    if choice == 'Sim' or choice == 'sim':
        qual = input('Qual filme deseja adicionar ? ')
        if Oscar.count(qual) != 0:
            return print('Este filme já está na lista !')
        indice = int(
            input('Em qual posição você deseja adiciona-lo ? Lembre-se que em python os índices começam em 0.'))
        Oscar.insert(indice, qual)
        print(Oscar)
    else:
        print('Então tá, tenha um bom filme.')


# Aula 3: - Perguntar a idade e classificá-la.

def idade():
    idade = int(input('Informe sua idade - apenas em números: '))

    if idade <= 11:
        print('Você é uma criança !')
    elif 60 <= idade:
        print('Você é um idoso !')
    elif idade < 20:
        print('Você é um adolescente !')
    else:
        print('Você é um adulto !')
    if idade < 0:
        raise ValueError('Por favor insira uma resposta válida !')


# idade()

# Next - Desejamos imprimir os números de 1 a 10.
for i in range(10):
    print(i)

Oscar = ['Pantera Negra', 'Infiltrado na Klan', 'Bohemian Rhapsody',
         'A favorita', 'Green Book', 'Roma', 'Nasce uma estrela', 'Vice']

# for titulo in Oscar:
#    print(titulo)

# for numero in range(1, 11):
#    print(numero)

# Problema - decompor em fatores primos.

'Esta função entra com um número inteiro entre 0 e 100, e retorna uma lista cujos elementos são \
os fatores primos dos mesmos'


# mudar para lista de todos os divisores e então testalos um a um afim de determinar quais são os primos dentre eles...
def dec_primo():
    numero = int(input('Digite um núemro: '))

    Decomposicao = []

    primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 39, 41, 43, 51]
    for p in range(len(primos)):
        while numero % primos[p] == 0:
            numero = numero / primos[p]
            Decomposicao.insert(p, primos[p])
        if numero % primos[p] != 0:
            primos.append(numero)

    return print('Sua decomposição em primos é: {}'.format(Decomposicao))


# dec_primo()

import math as mt
import time


def dec2_primo():
    t0 = time.time()

    numero = int(input('Digite um número: '))

    Decomposicao = []
    for p in range(2, mt.floor(numero) + 1):
        while numero % p == 0:
            Decomposicao.append(p)
            numero = numero / p
    if Decomposicao == []:
        Decomposicao.append(int(numero))

    t1 = time.time()
    return print(Decomposicao, t1 - t0)


dec2_primo()


# cópia do codigo apresentado em sala

# for n in range(2, limite_superior + 1):
#    if numero % n ==0 :
#        divisores.append(n)
#        numero = numero/2

# print(divisores)

# fatores_primos = []
# for divisor in divisores:
#    d_divisores = [1]
#    limite_superior = math.floor(numero/2.0)
#    for n in range(2, limite_superior + 1):
#        if divisor % n == 0:
#            d_divisores.appende(n)
#            divisor = divisor/n

def numbers():
    t1 = time.time()
    L = []
    N = int(input('Forneça um número natural N: '))
    for i in range(N + 1):
        L.insert(i, i)
    H = []
    for j in range(1, 11):
        Sl = []
        for item in L:
            if item % j == 0:
                Sl.append(item)
        H.append(Sl)
    t2 = time.time()
    t = t2 - t1
    i = 9
    print('Os múltiplos de {} estão na posição  {}'.format(i, i - 1))
    return H, t


M = [[1, 2, 3], [4, 2, 1], [1, 3, 5]]

for j in range(len(M)):
    M[1][j] = M[1][j] - 4 * M[0][j]

for j in range(len(M)):
    M[2][j] = M[2][j] - M[0][j]

for j in range(len(M)):
    M[1][j] = - M[1][j] / 6

for j in range(len(M)):
    M[2][j] = M[2][j] - M[1][j]


def eliminação_gaussiana(M):
    U = M
    n = len(U)
    for k in range(n - 1):
        if U[k][k] != 0:
            s = U[k][k]
            for j in range(n):
                U[k][j] = U[k][j] / s
        else:
            pass
        for i in range(k + 1, n):
            a = U[i][k]
            for j in range(n):
                U[i][j] = U[i][j] - a * U[k][j]
    return U


def general_gaussian_elimination(M):
    U = M
    n = len(U)

    L = [[0 for j in range(n)] for i in range(n)]
    for k in range(n):
        if U[k][k] != 0:
            s = U[k][k]
            L[k][k] = s
            for j in range(n):
                U[k][j] = U[k][j] / s
        else:
            pass
        for i in range(k + 1, n):
            a = U[i][k]
            L[i][k] = a / s
            for j in range(n):
                U[i][j] = U[i][j] - a * U[k][j]
    return L, U


# Aula 03/04:

lista = [38, -3, 5, 0, 47, 101, -53, 12, 8, -1]

novalista1 = [item + 1 for item in lista]

novalista2 = [item + 1 for item in lista if item >= 0]
# Somar 1 a cada elemento da lista, se o elemento for não negativo.
# Caso contrário, substituir o elemento por 0.

novalista3 = [item + 1 if item >= 0 else 0 for item in lista]

# Exemplo 3: Encontrar no Lipsum todas as palavras que começam com e ou E.

lipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et " \
         "dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex " \
         "ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu " \
         "fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt " \
         "mollit anim id est laborum. "
list = [lipsum.split()]

novalista4 = [word for word in list if word[0].lower() == 'e']
novalista_exemplo1 = ['elit,', 'eiusmod', 'et', 'enim', 'exercitation', 'ex', 'ea', 'esse', 'eu', 'Excepteur', 'est']
novalista5 = [word for word in list if len(word) < 4]
novalista_exemplo2 = ['sit', 'sed', 'do', 'ut', 'et', 'Ut', 'ad', 'ut', 'ex', 'ea', 'in', 'in', 'eu', 'non', 'in',
                      'qui', 'id', 'est']

novalista = list(set(novalista5))

Matriz = [[1, 2], [2, 4]]

# Calcula a matriz transposta de uma dada matriz dada.
Matriz_transposta = [[linha[i] for linha in Matriz] for i in range(len(Matriz[0]))]

# Aula - 09/04 - Paradigmas de Programação.

# Imperativo:

# - Estruturada (Matlab, C, Pascal, Fortran 77-90)
# - Orientação objetos (Java, Python)
# - Funcional (Lisp, Haskell, Scala, Python)

# Declarativa:

# - Funcional
# - Lógico (Prolog)


# Aula 10/04

# 1 Produto interno
# 2 Produto matriz vetor
# 3 Produto matricial

# 1 Implemantar a multiplicação de matrizes;
# 2 Aplicar 1 para matrizes grandes e comparar com np.dot;
# 3 implementar a eliminação gaussiana.
import numpy as np


def inner(x, y):
    s = 0
    for i in range(len(x)):
        s += x[i] * y[i]
    return s


def iner_m_v(A, x):
    V = np.zeros(len(x))
    for i in range(len(A)):
        for j in range(len(x)):
            V[i] = inner(A[i], x)
    return V


def mult(A, B):
    if np.shape(A)[1] != np.shape(B)[0]:
        return print("As matrizes não podem ser multiplicadas dessa forma !")
    m = np.shape(A)[0]
    n = np.shape(B)[1]
    M = np.zeros((m, n))
    for i in range(m):
        for j in range(n):
            M[i, j] = inner(A[i], B[j])
    return M


def numpy_general_gaussian_elimination(X):
    U = X
    n = len(U)

    L = np.zeros((n, n))
    for k in range(n):
        if U[k, k] != 0:
            s = U[k, k]
            L[k, k] = s
            for j in range(n):
                U[k, j] = U[k, j] / s
        else:
            pass
        for i in range(k + 1, n):
            s = U[k, k]
            a = U[i, k]
            L[i, k] = a / s
            for j in range(n):
                U[i, j] = U[i, j] - a * U[k, j]
    return L, U


# Eliminação Gaussiana com permutação generalizada: P*A = L*U - A retangular (m x n);
# n: número de linhas;
# m: Número de colunas.
# Pe := np.array(n); # l-ézimma matriz de permutação;

'Outputs'
# P := np.array(n); # Matriz de permutação no estágio final da Eliminação;
# L := np.array(n); # Matriz triangular inferior dos fatores;
# U := np.array(1..n,1..n); # Matriz triangular superior dos fatores, no estágio final da eliminação

def G_el(X):
    # Cria a matriz de saída U (m x n).
    U = np.array(X, dtype=float)

    # Defini-se as dimensões m e n da matriz.
    (n, m) = U.shape

    # Geração das matrizes de saída P e L, onde P é matriz de permutação e L matriz das transformaçõe elementares.
    L = np.eye(n)
    P = np.eye(n)

    # k varia sobre as colunas de U, buscando seus pivôs.
    for k in range(m):

        # Se um de seus pivôs for zero, procura-se na mesma coluna um índice i de modo que
        # o elemento de U correspondente seja diferente de 0. Aplica-se então uma troca de linhas afim de defini-lo
        # como novo pivô.
        if U[k, k] == 0:
            Pe = np.eye(n)
            i = k
            while U[i, i] == 0:
                i += 1
            # Troca de linhas:
            p1 = np.array(P[i, :])
            p2 = np.array(P[k, :])
            Pe[i, :] = p2
            Pe[k, :] = p1
            U = np.dot(Pe, U)
            P = np.dot(Pe, P)
        # Caso não haja elemento nulo no candidato à pivô, continuamos normalmente:
        else:
            # simplificando a linha do pivô, afim de transforma-lo em 1.
            a = U[k, k]
            L[k, k] = a
            U[k, :] = U[k, :] * (1 / a)

            # Zerando os elementos abaixo do pivô, e subtraindo a linha do pivô das demais linhas abaixo.
            for i in range(k + 1, n):
                b = U[i, k]
                L[i, k] = b
                U[i, :] = U[i, :] - b * U[k, :]

    return P, L, U


A = [[3.0, 5, 7], [1, 2, 3], [7, 9, 1]]

# Encontrar as soluções dos sistemas lineares propostos usando a função 'solve' e também usando a função LU.
import scipy.linalg as sp

def Solve_LU(A, b):
    P, L, U = sp.lu(A)
    Xlu = sp.solve(U, sp.solve(L, P @ b))
    return Xlu

#   Produto de Kronecker.
