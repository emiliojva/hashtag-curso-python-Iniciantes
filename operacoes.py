'''
Basic operations in Python
'''
faturamento = 1000
custo = 700
novas_vendas = 300

faturamento = faturamento + novas_vendas # adicao
imposto = faturamento * 0.1  # multiplicacao
print("Imposto a pagar: R$" + str(imposto) + " do faturamento R$" + str(faturamento))
lucro = faturamento - custo # subtracao
margem_lucro = lucro / faturamento # divisao
restituicao = imposto * 0.1 # porcentagem

# mod ou %
resto = faturamento % 3  # resto da divisao

# exponenciacao
exponenciacao = 2 ** 3  # 2 elevado a 3 = 8

tempo_em_meses = 160
tempo_em_anos = int(tempo_em_meses / 12)  # conversao de meses para anos
print("Tempo em anos:", tempo_em_anos)
print(tempo_em_meses % 12, "meses restantes")

numero_pra_menos = 123.22
print("round(123.22) Arrendonda pra menos",round(numero_pra_menos))  # arredondamento = 123
numero_pra_mais = 123.78
print("round(123.78) Arrendonda pra mais",round(numero_pra_mais))  # arredondamento = 124

# python entende edicao visual
valor_visual = 139_018_182 # python entende o valor como 139018182


print("Faturamento:", faturamento)
print("Custo:", custo)
print("Lucro:", lucro)
print("Margem de lucro:", margem_lucro * 100, "%")

