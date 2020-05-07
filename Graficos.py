import numpy as np
import matplotlib.pyplot as plt


def Taylor_cosseno(n):
    def fat(int):
        p = 1
        for j in range(1, int + 1):
            p *= j
        return p
    x = np.linspace(-8, 8, 1000)

    fig = plt.figure()
    for m in range(1, n + 1):
        cosx = []
        for item in x:
            Soma = 0
            for i in range(m):
                Soma += ((-1) ** i) * (item ** (2 * i)) / fat(2 * i)
            cosx.append(Soma)
        plt.plot(x, cosx)

    plt.axis([-8, 8, -1, 1])
    return plt.show()


Taylor_cosseno(20)
