# Usado para plotar o gráfico no PyCharm
import matplotlib.pyplot as plt
import numpy as np
from skfuzzy import control as ctrl

# Antecedentes
temperatura = ctrl.Antecedent(np.arange(0,38,1), "temperatura")
humidade = ctrl.Antecedent(np.arange(0,101,1), "humidade")

# consequente
potencia = ctrl.Consequent(np.arange(0,101,1), "Potência ar condicionado")

temperatura.automf(3, names=["Baixa", "Media", "Alta"])
humidade.automf(3, names=["Baixa", "Media", "Alta"])
potencia.automf(3, names=["Baixa", "Media", "Alta"])

# plotando grafico
temperatura.view()
humidade.view()
potencia.view()
plt.show()


# criando regras
# Coluna0 (Baixa) X ( Linha0, Linha1 e Linha2)
ruleTempBaixa1 = ctrl.Rule(temperatura["Baixa"] & humidade["Baixa"], potencia["Alta"])
ruleTempBaixa2 = ctrl.Rule(temperatura["Baixa"] & humidade["Media"], potencia["Alta"])
ruleTempBaixa3 = ctrl.Rule(temperatura["Baixa"] & humidade["Alta"], potencia["Media"])

# Coluna1 (Média) X ( Linha0, Linha1 e Linha2)
ruleTempMedia1 = ctrl.Rule(temperatura["Media"] & humidade["Baixa"], potencia["Baixa"])
ruleTempMedia2 = ctrl.Rule(temperatura["Media"] & humidade["Media"], potencia["Baixa"])
ruleTempMedia3 = ctrl.Rule(temperatura["Media"] & humidade["Alta"], potencia["Media"])

# Coluna1 (Alta) X ( Linha0, Linha1 e Linha2)
ruleTempAlta1 = ctrl.Rule(temperatura["Alta"] & humidade["Baixa"], potencia["Baixa"])
ruleTempAlta2 = ctrl.Rule(temperatura["Alta"] & humidade["Media"], potencia["Media"])
ruleTempAlta3 = ctrl.Rule(temperatura["Alta"] & humidade["Alta"], potencia["Alta"])

# Criando o Sistema
potenciaArCondicionado_ctrl = ctrl.ControlSystem([ruleTempBaixa1, ruleTempBaixa2, ruleTempBaixa3,
                                                  ruleTempMedia1, ruleTempMedia2, ruleTempMedia3,
                                                  ruleTempAlta1, ruleTempAlta2, ruleTempAlta3])
potenciaArCondicionado = ctrl.ControlSystemSimulation(potenciaArCondicionado_ctrl)

potenciaArCondicionado.input["temperatura"] = 20
potenciaArCondicionado.input["humidade"] = 30
potenciaArCondicionado.compute()
print("A potencia do ar é: ", potenciaArCondicionado.output["Potência ar condicionado"])
potencia.view(sim=potenciaArCondicionado)
plt.show()

potenciaArCondicionado.input["temperatura"] = 30
potenciaArCondicionado.input["humidade"] = 15
potenciaArCondicionado.compute()
print("A potencia do ar é: ", potenciaArCondicionado.output["Potência ar condicionado"])
potencia.view(sim=potenciaArCondicionado)
plt.show()

potenciaArCondicionado.input["temperatura"] = 35
potenciaArCondicionado.input["humidade"] = 30
potenciaArCondicionado.compute()
print("A potencia do ar é: ", potenciaArCondicionado.output["Potência ar condicionado"])
potencia.view(sim=potenciaArCondicionado)
plt.show()

potenciaArCondicionado.input["temperatura"] = 10
potenciaArCondicionado.input["humidade"] = 70
potenciaArCondicionado.compute()
print("A potencia do ar é: ", potenciaArCondicionado.output["Potência ar condicionado"])
potencia.view(sim=potenciaArCondicionado)
plt.show()