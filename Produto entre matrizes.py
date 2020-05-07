
# Matriz (3 x 2)
A = [[1, 2], [3, 4], [5, 6]]

# Matriz (2 x 2)
B = [[1, 4], [5, 1]]

# Matriz (2 x 3)
B2 = [[1, 3, 6], [4, 5, 3]]

# Seguem o produto matricial AB e AB2 como exemplos para cada método de produto matricial abaixo.

'Observação: Todos os vetores de n elementos serão qui expressos como listas de n elementos, sejam eles vetores \
 (n x 1) ou (1 x n), sendo mencionando suas dimensões em cada método, afim de que haja consistência. '


# Produto vetorial - entrada a entrada.
# entrada: vetores x e y de mesma dimensão.
# saída: escalar correspondente ao produto interno usual de x por y.

def xy(x, y):
    # Verificação se as dimensões são compatíveis para o produto. (ou seja, comprimento de x e y são iguais.)
    if len(x) != len(y):
        return print('Erro: Dimensões entre os vetores incompatíveis para o produto !')

    Soma = 0
    # Soma:= < x , y > = Somatório de i = 0 até i = (n - 1) de x(i) * y(i), com n sendo o 'tamanho' de x.
    for k in range(len(x)):
        Soma += x[k] * y[k]
    return Soma


# ---------------------------------------------------

# Produto matriz vetor.
# Entrada matriz A (m x n) e vetor x (n x 1). (aqui representado como uma lista x de n elementos.)
# Saída: Vetor Ax (m x 1) (aqui representado como uma lista de m elementos).

def ax(matriz1, x):
    # m: Número de linhas da matriz1;
    # n: número de colunas da matriz1;
    # p: tamanho do vetor x, 'número de elementos em x'.

    m = len(matriz1)
    n = len(matriz1[0])
    p = len(x)

    # Verificação se as dimensões da matriz1 e x são compatíveis para o produto.
    if n != p:
        return print('Erro: Dimensões entre matriz e vetor incompatíveis para o produto !')

    # Ax: vetor resultante do produto matriz1*x.
    Ax = []
    for i in range(m):
        # Cada i-ésima entrada do vetor resultante Ax é o produto vetorial da i-ésima linha de matriz1 com x.
        # Lembrando que cada matriz1[i] representa a i-ésima linha da matriz matriz1.
        Ax.append(xy(matriz1[i], x))

    return Ax


# ---------------------------------------------------

# Produto vetor matriz.
# Entrada vetor x (1 x m) (aqui representado como uma lista de m elementos )e matriz A (m x n).
# Saída: Vetor xA (1 x n) (aqui representado como uma lista de n elementos ).

def xa(x, matriz1):
    # m: Número de linhas de matriz1;
    # n: número de colunas de matriz1;
    # p: tamanho do vetor x, 'número de elementos em x'.

    m = len(matriz1)
    n = len(matriz1[0])
    p = len(x)

    # Verificação se as dimensões de matriz1 e x são compatíveis para o produto.
    if p != m:
        return print('Erro: Dimensões entre vetor e matriz incompatíveis para o produto !')

    # xA: vetor resultante do produto x*matriz1.
    xA = []
    for j in range(n):
        # vetor (m x 1) e lista de m elementos, representando a j-ésima coluna de matriz1.
        coluna_j_de_A = [matriz1[k][j] for k in range(m)]

        # Cada j-ésima entrada do vetor resultante xA é o produto vetorial de x com  j-ésima coluna de matriz1.
        xA.append(xy(x, coluna_j_de_A))

    return xA


# ------------------------------------------------------------------------------------------------------------------
# Produtos Matriciais.
# ------------------------------------------------------------------------------------------------------------------
# 1º Produto matricial : definição
'Toma como entradas, matrizes A,B de dimensões (m x n) e (p x q) respectivamente, e calcula o produto matricial ' \
    'AB onde cada AB(i,j) é somatório de k = 0 até (n - 1) de cada A(i, k) * B(k, j).'


def prod_matriz1(matriz1, matriz2):
    m = len(matriz1)
    n = len(matriz1[0])

    p = len(matriz2)
    q = len(matriz2[0])

    # Verificação se as dimensões de matriz1 e matriz2 são compatíveis para o produto.
    if n != p:
        return print(
            "Erro: Dimensões entre matrizes incompatíveis para o produto, favor verificar as características de "
            "entrada.")

    # Produto matricial matriz1*matriz2.
    AB = []
    for i in range(m):
        # i-ésima linha de matriz1*matriz2.
        Linha_de_AB = []
        for j in range(q):

            # Elemento AB(i,j)
            Soma = 0
            for k in range(n):
                Soma += matriz1[i][k] * matriz2[k][j]

            # Adicionando j-ésimos elementos matriz1(i,j) na i-ésima linha de matriz1*matriz2.
            Linha_de_AB.append(Soma)

        # Adicionando-se a i-ésimo linha Linha_de_AB.
        AB.append(Linha_de_AB)
    return AB


print(prod_matriz1(A, B))
print(prod_matriz1(A, B2))

# ------------------------------------------------------------------------------------------------------------------
# 2º Produto matricial : definição
'Toma como entradas, matrizes A,B de dimensões (m x n) e (p x q) respectivamente, e calcula o produto matricial ' \
    'AB onde cada AB(i,j) é o produto entre a i-ésima linha A e a j-ésima coluna de B'


def prod_matriz2(matriz1, matriz2):
    m = len(matriz1)
    n = len(matriz1[0])

    p = len(matriz2)
    q = len(matriz2[0])

    # Verificação se as dimensões de matriz1 e matriz2 são compatíveis para o produto.
    if n != p:
        return print(
            "Erro: Dimensões entre matrizes incompatíveis para o produto, favor verificar as características de "
            "entrada.")

    # Produto matricial matriz1*matriz2.
    AB = []
    for i in range(m):
        # i-ésima linha de matriz1*matriz2.
        i_Linha_de_AB = []
        for j in range(q):
            # j-ésima coluna de matriz1*matriz2.
            j_Coluna_de_B = [matriz2[k][j] for k in range(n)]
            # Cada entrada da matriz AB(i,j) é o produto interno da i-ésima linha de matriz1 com a j-ésima coluna de
            # matriz2, ou seja (xy(matriz1[i], j_Coluna_de_B) onde xy é a função produto interno entre x e y.

            i_Linha_de_AB.append(xy(matriz1[i], j_Coluna_de_B))

        # Adicionando-se a i-ésima linha de AB, AB[i] = i_Linha_de_AB.
        AB.append(i_Linha_de_AB)
    return AB


print(prod_matriz2(A, B))
print(prod_matriz2(A, B2))

# ------------------------------------------------------------------------------------------------------------------
# 3º Produto matricial : definição
'Toma como entradas, matrizes A,B de dimensões (m x n) e (p x q) respectivamente, e calcula o produto matricial ' \
    'AB onde cada j-ésima coluna de AB é o produto entre a matriz A e a j-ésima coluna de B.'


def prod_matriz3(matriz1, matriz2):
    n = len(matriz1[0])

    p = len(matriz2)
    q = len(matriz2[0])

    # Verificação se as dimensões de matriz1 e matriz2 são compatíveis para o produto.
    if n != p:
        return print(
            "Erro: Dimensões entre matrizes incompatíveis para o produto, favor verificar as características de "
            "entrada.")

    # Adicionaremos as j-ésima colunas de AB como sendo as j-ésima linhas de AB transposta.
    AB_Transposta = []
    for j in range(q):
        # Lembrando que aqui as j-ésima colunas de de AB, são as j-ésima linhas de AB transposta.
        Coluna_j_de_B = [matriz2[k][j] for k in range(n)]

        # j-ésima coluna de AB é o produto entre a matriz matriz1 e a j-ésima coluna de matriz2.
        Coluna_j_de_AB = ax(matriz1, Coluna_j_de_B)

        # Agora adicionaremos Coluna_j_de_AB como j-ésima linha de AB transposta.
        AB_Transposta.append(Coluna_j_de_AB)

    # Transpomos a matriz transposta de AB, afim de resgatermos a matriz AB agora com as devidas linhas.
    AB = [[linha[i] for linha in AB_Transposta] for i in range(len(AB_Transposta[0]))]

    return AB


print(prod_matriz3(A, B))
print(prod_matriz3(A, B2))

# ------------------------------------------------------------------------------------------------------------------
# 4º Produto matricial : definição
'Toma como entradas, matrizes A,B de dimensões (m x n) e (p x q) respectivamente, e calcula o produto matricial ' \
    'AB onde cada i-ésima linha de AB é o produto da i-ésima linha de A com a matriz B.'


def prod_matriz4(matriz1, matriz2):
    m = len(matriz1)
    n = len(matriz1[0])

    p = len(matriz2)

    # Verificação se as dimensões de matriz1 e matriz2 são compatíveis para o produto.
    if n != p:
        return print(
            "Erro: Dimensões entre matrizes incompatíveis para o produto, favor verificar as características de "
            "entrada !")

    # Produto matricial matriz1*matriz2.
    AB = []
    for i in range(m):
        # i-ésima linha de AB é o produto entre a i-ésima linha de matriz1 com a matriz matriz2, ou seja
        # xA(matriz1[i], matriz2) onde matriz1[i] é a i-ésima linha de matriz1.
        Linha_i_de_AB = xa(matriz1[i], matriz2)

        # Aciona-se esta i-ésima linha de AB na matriz AB.
        AB.append(Linha_i_de_AB)
    return AB


print(prod_matriz4(A, B))
print(prod_matriz4(A, B2))
