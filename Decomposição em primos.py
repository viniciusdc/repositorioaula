import math


def prime_dec(n):
    """Decomposição em fatores primos./
     Esta função retorna o máximo fator primo na decomposição em fatores primos de n.

     Parametros:
     ------------
     n - número inteiro diferente de 0 e 1.

     Retorna:
     ------------
     Maior_primo: maior fator primo na decomposição de n.

     Exemplos de entrada:
     ------------
     Para n = 100, temos que n = 2*2*5*5, ou seja, o máximo dos fatores primos de n (são eles 2 e 5) é 5.
     Logo, prime_dec(100) = 5.

     Para n = 13195, temos que n = 5*7*13*29, ou seja, o máximo dos fatores primos de n é 29.
     Logo, prime_dec(13195) = 29.

     Para n = 14586, temos que n = 2*3*11*13*17, ou seja, o máximo dos fatores primos de n é 17.
     Logo, prime_dec(14586).

     Todos os métodos acima utilizam da primeira forma de variação.

     porém note que para n = 153, temos que n = 3*3*17, ou seja, o máximo dos fatores primos de n é 17.
     Logo, prime_dec(153) e dado que 17 > sqrt(153) utilizamos a segunda forma de variação.
     """

    # A menos do fator -1, a decomposição em primos de n e -n é idêntica.
    n = abs(n)
    Check_N = n
    # Verificação se n está de acordo com as especificações da função.
    if n == 0 or n == 1:
        raise Exception('O número {} de entrada não condiz com as especificações da função !'.format(n))

    # Se todos os fatores primos p de n, são tais que p <= sqrt(n).
    #  então variamos os possíveis primos eu sua decomposição, começando de 2 até sqrt(n).

    # se a condição acima for satisfeita, optaremos pelo método abaixo, afim de maior rapidez no processo,
    # uma vez que, em alguns casos, variar os indices desse modo pode ser muito mais eficiente do que ir até [n/2].

    # Definindo lista dos fatores primos de n, sem repetição.
    Lista_de_primos = []
    # Expoentes armazena o expoente de cada fator primo para verificação posterior.
    Expoentes = []

    # Percorre-se os inteiros de 2 à ((raiz de n) + 1), - Começa-se de 2, pois 2 é o menor dos fatores primos possiveis.
    # procurando os primos p que pertençam a decomposição de n, i.e, p | n.
    for i in range(2, int(math.sqrt(n)) + 1):
        # Se i | n, então:

        if n % i == 0:
            # Adiciona-se esse número a lista de primos de n, sabemos que este número i, é fator primo de n,
            # pois estamos seguindo de forma ordenada a decomposição de n.
            Lista_de_primos.append(i)
            c = 0
            while n % i == 0:
                # Este passo elimina fatores primos repetidos da lista, assim como as potências desse mesmo primo
                # em n, garantindo que o próximo i tal que i | n, será obrigatoriamente um primo.
                n = n / i
                c += 1
            Expoentes.append(c)

    # Verificação se o produto dos fatores primos com seus respectivos expoentes equivale ao valor de entrada n.
    # Para isso observaremos se n / (P1 * P2 * ... Pn) = 1. Implicando que todos os primos em sua decomposição foram
    # avaliados corretamente.

    # Caso a verificação seja bem sucedida, retorna-se o máximo primo desta decomposição.
    if int(n) == 1:
        'Caso deseje ver a lista de fatores primos e seus expoentes, retire o sinal de # dos itens abaixo abaixo.'
        # print('A lista de fatores primos e seus respectivos expoentes na decomposição de {} são: {},{}'
        #      .format(Check_N, Lista_de_primos, Expoentes))

        # print('Uso do 1º método') - retire o comentário caso deseje ver qual variação está sendo usada para cada n.
        return print('O maior fator primo na decomposição  de {} é: {}'.format(Check_N, max(Lista_de_primos)))

    # caso contrário, temos que existe pelo menos um fator primo P de n de modo que P > sqrt(n), continuaremos
    # o processo do último primo encontrado até ([n/2] + 1) garantindo assim todos os possíveis fatores primos de n.
    else:
        n = Check_N
        # print('Uso do 2º método') - retire o comentário caso deseje ver qual variação está sendo usada para cada n.

        # Percorre-se os inteiros de (sqrt(n) + 1 ) até ([n/2] + 1), - Começa-se de 2, pois 2 é o menor dos fatores
        # primos possiveis. procurando os primos p que pertençam a decomposição de n, i.e, p | n.
        for i in range(int(math.sqrt(n)) + 1, math.floor(n / 2) + 1):
            # Se i | n, então:

            if n % i == 0:
                # Adiciona-se esse número a lista de primos de n, sabemos que este número i, é fator primo de n,
                # pois estamos seguindo de forma ordenada a decomposição de n.
                Lista_de_primos.append(i)

                c = 0
                while n % i == 0:
                    # Este passo elimina fatores primos repetidos da lista, assim como as potências desse mesmo primo
                    # em n, garantindo que o próximo i tal que i | n, será obrigatoriamente um primo.
                    n = n / i
                    c += 1
                Expoentes.append(c)

        # é possível que n já seja um número primo, neste caso todas as medidas tomadas anteriormente resultarão em uma
        # lista de primos vazia, assim devemos adicionar n de forma manual a lista e este será portanto a máximo
        # primo em sua decomposição.
        if len(Lista_de_primos) == 0:
            Lista_de_primos.append(Check_N)
            Expoentes.append(1)

        'Caso deseje ver a lista de fatores primos e seus expoentes, retire o sinal de # dos print abaixo.'
        # print('A lista de fatores primos e seus respectivos expoentes na decomposição de {} são: {},{}'
        #      .format(Check_N, Lista_de_primos, Expoentes))

        return print('O maior fator primo na decomposição de {} é: {}'.format(Check_N, max(Lista_de_primos)))


# Exemplos interessantes:
# prime_dec(11)
# prime_dec(126)
# prime_dec(13195)
# prime_dec(62)
# prime_dec(153)
# prime_dec(3000007)

# exemplo para apenas a variação 2:
# prime_dec(12456328)

# Exemplo muito bom para a variação 1:
# prime_dec(14586)

# Teste para N = 600851475143,
prime_dec(600851475143)
