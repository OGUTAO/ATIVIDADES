#Questão 3: 
#Python

import json



def faturamento(dados):

    valores = [dia['valor'] for dia in dados if dia['valor'] > 0]



    menor_faturamento = min(valores)

    maior_faturamento = max(valores)



    media_mensal = sum(valores) / len(valores)



    dias_acima_da_media = sum(1 for valor in valores if valor > media_mensal)



    return menor_faturamento, maior_faturamento, dias_acima_da_media



with open('faturamento.json', 'r') as f:

    dados = json.load(f)



menor_faturamento, maior_faturamento, dias_acima_da_media = faturamento(dados)



print(f"Menor valor de faturamento: R$ {menor_faturamento:.2f}")

print(f"Maior valor de faturamento: R$ {maior_faturamento:.2f}")

print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")

