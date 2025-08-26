# 2.1.1 str - Texto
print("2.1.1 string - Texto")
nome_empresa = "Minha Empresa"
print("Nome da empresa:", nome_empresa)
print("--------------------------------------------")

# 2.1.2 int - Números inteiros
print("2.1.2 int - Números inteiros")
faturamento = 0
ativo = 1500
passivo = 700
print("Faturamento inicial:", faturamento)
faturamento = ativo - passivo
print("Faturamento:", faturamento)
print("--------------------------------------------")

# 2.1.3 float - Números decimais
print("2.1.3 float - Números decimais")
novas_vendas = 300
print("Novas vendas:", novas_vendas)
faturamento += novas_vendas
custo = 770
taxa_imposto = 0.1
imposto = taxa_imposto * faturamento
print("Imposto a pagar:", imposto)
print("Faturamento:", faturamento)
print("Custo:", custo)
print("Lucro:", faturamento - custo - imposto)
print("O faturamento foi:",faturamento, "reais")
print("--------------------------------------------")

# 2.1.4 bool - Verdadeiro ou falso - False | True
print("2.1.4 boolean - Verdadeiro ou falso")
ativo_positivo = faturamento > 0
print("Ativo positivo:", "Sim" if ativo_positivo else "Não")
print("--------------------------------------------")

# 2.1.5 NoneType - Ausência de valor
print("2.1.5 NoneType - Ausência de valor")
valor_nulo = None
print("Valor nulo:", valor_nulo)
print("--------------------------------------------")