from math import e
import math

an = 0.00000
bn = 0.00000
xn = 0.00000

# condição de parada
parada = 0.001
precParada = 3

# PRECISÃO DE CASAS DECIMAIS
prec = 6


def calc(cont, xk, aux, stopCond):
    # ENTRE COM A FUNÇÃO AQUI
    func = 2*(xk ** 3) + 3*(xk ** 2) - 0.5
    revFunc = 6*(xk ** 2) + 6*xk # Derivada da função
    if cont == 0:
        stopFunc = round(abs(func), precParada)
        if (stopFunc <= parada):
            exit()
    print("------------------------------------------")
    print("X",cont," = ", round(xk, prec))
    print("F(x",cont,") = ", round(func, prec))
    if cont != 0:
        print("F'(x", cont, ") = ", round(revFunc, prec))
    if aux != None:
        mod = xk - aux
        print("| ", xk, " - ", aux, " | = ", round(abs(mod), prec))
    print("------------------------------------------")

    if cont != 0:
        if stopCond == 1:
            stopFunc = round(abs(func), precParada)
            if (stopFunc < parada):
                exit()
        elif stopCond == 2:
            mod = xk - aux
            stopAbs = round(abs(mod), precParada)
            if (stopAbs < parada):
                exit()
        else:
            mod = xk - aux
            stopAbs = round(abs(mod), precParada)
            stopFunc = round(abs(func), precParada)
            if (stopAbs <= parada):
                print("Parei em MODULO")
                exit()
            elif (stopFunc <= parada):
                print(stopFunc)
                print(parada)
                print("Parei em FUNÇÃO")
                exit()


    aux = xk
    xk = xk - func/revFunc
    cont += 1

    calc(cont, xk, aux, stopCond)
    print("-------------------------------------")


if __name__ == '__main__':
    xk = float(input("Entre com o valor inicial: "))
    cont = 0
    ### stopCond -> 0 para ambos // 1 para Func < parada // 2 para |xn - xn-1| < parada
    stopCond = 1
    calc(cont, xk, None, stopCond)