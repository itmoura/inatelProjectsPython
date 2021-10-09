"""
    NP2 - C210
    Código referente a Questão 1
"""

# Usado para plotar o gráfico no PyCharm
import matplotlib.pyplot as plt
import numpy as np
from skfuzzy import control as ctrl

# Antecedentes
nivelTanque = ctrl.Antecedent(np.arange(0,101,1), "nivel do tanque")
erroLeitura = ctrl.Antecedent(np.arange(0,101,1), "erro de leitura")

# consequente
bomba = ctrl.Consequent(np.arange(0,101,1), "potência da bomba")

nivelTanque.automf(3, names=["baixo", "medio", "alto"])
erroLeitura.automf(3, names=["baixo", "medio", "alto"])
bomba.automf(3, names=["baixo", "medio", "alto"])

# plotando grafico
nivelTanque.view()
erroLeitura.view()
bomba.view()
plt.show()


# criando regras
# Coluna0 (Baixa) X ( Linha0, Linha1 e Linha2)
rule1 = ctrl.Rule(nivelTanque["baixo"] & erroLeitura["baixo"], bomba["alto"])
rule2 = ctrl.Rule(nivelTanque["alto"] | erroLeitura["baixo"], bomba["baixo"])
rule3 = ctrl.Rule(nivelTanque["medio"] | erroLeitura["medio"], bomba["medio"])

# Criando o Sistema
bomba_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
potenciaBomba = ctrl.ControlSystemSimulation(bomba_ctrl)

# A) Nível do tanque: 50; Erro de leitura: 10
potenciaBomba.input["nivel do tanque"] = 50
potenciaBomba.input["erro de leitura"] = 10
potenciaBomba.compute()
print("A potencia da bomba é: ", potenciaBomba.output["potência da bomba"], "%")
bomba.view(sim=potenciaBomba)
plt.show()

# B) Nível do tanque: 80; Erro de leitura: 20
potenciaBomba.input["nivel do tanque"] = 80
potenciaBomba.input["erro de leitura"] = 20
potenciaBomba.compute()
print("A potencia da bomba é: ", potenciaBomba.output["potência da bomba"], "%")
bomba.view(sim=potenciaBomba)
plt.show()

# C) Nível do tanque: 10; Erro de leitura: 50
potenciaBomba.input["nivel do tanque"] = 10
potenciaBomba.input["erro de leitura"] = 50
potenciaBomba.compute()
print("A potencia da bomba é: ", potenciaBomba.output["potência da bomba"], "%")
bomba.view(sim=potenciaBomba)
plt.show()