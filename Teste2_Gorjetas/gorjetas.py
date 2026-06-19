quantGarc = int(input("Indique quantos garçons receberam gorjetas: "))
totalGorj = float(input("Insira o valor total de gorjetas em reais: "))

def calcular_divisao_gorjeta(totalGorj, numGarc):
    if numGarc <= 0:
        raise ValueError("O número de garçons deve ser maior que zero.")
    if totalGorj < 0:
        raise ValueError("O valor da gorjeta não pode ser negativo.")

calcular_divisao_gorjeta(totalGorj, quantGarc)

valorBase = totalGorj/quantGarc
import math
valorFinal= math.trunc(valorBase)
print(f"Cada garçom irá receber: R${valorFinal},00")

premiacao = math.trunc((totalGorj - (valorFinal * quantGarc)) * 100) / 100
print(f"O garçom mais efetivo receberá: R${premiacao}")