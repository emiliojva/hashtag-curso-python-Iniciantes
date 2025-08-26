# ⚙️ Aula 02 - Operadores e Operações

## 🎯 Objetivos da Aula
- Dominar operadores matemáticos
- Aprender operadores de atribuição compostos
- Entender o operador ternário Python
- Comparar com operadores PHP

---

## ➕ Operadores Matemáticos

### **Operadores básicos:**
```python
# Operações básicas
soma = 10 + 5        # 15
subtracao = 10 - 5   # 5
multiplicacao = 10 * 5  # 50
divisao = 10 / 5     # 2.0 (sempre float)

# Operadores especiais Python
divisao_inteira = 10 // 3  # 3 (sem resto)
resto = 10 % 3            # 1 (módulo)
potencia = 2 ** 3         # 8 (exponenciação)
```

### **Comparação PHP → Python:**
```php
// PHP
$divisao = 10 / 5;      // 2 (int se exato)
$resto = 10 % 3;        // 1
$potencia = pow(2, 3);  // 8
```

```python
# Python
divisao = 10 / 5        # 2.0 (sempre float)
resto = 10 % 3          # 1
potencia = 2 ** 3       # 8 (operador nativo)
```

---

## 🔄 Operadores de Atribuição

### **Operadores compostos:**
```python
# Atribuição composta (igual ao PHP)
numero = 10
numero += 5    # numero = numero + 5  → 15
numero -= 3    # numero = numero - 3  → 12
numero *= 2    # numero = numero * 2  → 24
numero /= 4    # numero = numero / 4  → 6.0
numero //= 2   # numero = numero // 2 → 3.0
numero %= 2    # numero = numero % 2  → 1.0
numero **= 3   # numero = numero ** 3 → 1.0
```

### **Com strings (diferença do PHP):**
```php
// PHP - Concatenação
$texto = "Olá";
$texto .= " Mundo";  // "Olá Mundo"
```

```python
# Python - Concatenação
texto = "Olá"
texto += " Mundo"    # "Olá Mundo"
```

---

## ❓ Operador Ternário

### **Sintaxe diferente do PHP:**
```php
// PHP
$resultado = $condicao ? "verdadeiro" : "falso";
$status = $idade >= 18 ? "Adulto" : "Menor";
```

```python
# Python - ordem diferente!
resultado = "verdadeiro" if condicao else "falso"
status = "Adulto" if idade >= 18 else "Menor"
```

### **Estrutura Python:**
```python
valor_se_verdadeiro if condicao else valor_se_falso
```

### **Exemplos práticos:**
```python
# Verificações simples
idade = 20
categoria = "Adulto" if idade >= 18 else "Menor"

# Valores numéricos
saldo = 150
taxa = 0.1 if saldo > 100 else 0.05

# Validações
nota = 8.5
situacao = "Aprovado" if nota >= 7 else "Reprovado"

# String formatting
nome = "João"
mensagem = f"Bem-vindo, {nome}!" if nome else "Usuário não identificado"
```

---

## 🔢 Funções Matemáticas Úteis

### **Conversões de tipo:**
```python
# Conversões explícitas
idade_str = "25"
idade_int = int(idade_str)        # 25
preco_str = "19.99"
preco_float = float(preco_str)    # 19.99

# Conversão para string
numero = 42
texto = str(numero)               # "42"
```

### **Funções built-in:**
```python
# Arredondamento
numero = 123.456
arredondado = round(numero)       # 123
com_casas = round(numero, 2)      # 123.46

# Valores absolutos
negativo = -10
positivo = abs(negativo)          # 10

# Min/Max
menor = min(10, 5, 8)            # 5
maior = max(10, 5, 8)            # 10
```

---

## ✅ Exercícios Práticos

### **1. Calculadora básica:**
```python
# Simulação financeira
faturamento = 1000
custo = 700
novas_vendas = 300

# Usar operadores compostos
faturamento += novas_vendas
imposto = faturamento * 0.1
lucro = faturamento - custo - imposto
margem = (lucro / faturamento) * 100

print(f"Faturamento total: R$ {faturamento}")
print(f"Lucro: R$ {lucro:.2f}")
print(f"Margem: {margem:.1f}%")
```

### **2. Conversões e validações:**
```python
# Conversão de tempo
tempo_meses = 160
tempo_anos = tempo_meses // 12
meses_restantes = tempo_meses % 12

print(f"Tempo: {tempo_anos} anos e {meses_restantes} meses")

# Validações com ternário
idade = 17
pode_dirigir = "Sim" if idade >= 18 else "Não"
print(f"Pode dirigir: {pode_dirigir}")
```

### **3. Formatação de números:**
```python
# Números grandes com separadores visuais
valor_grande = 139_018_182  # Python permite _
print(f"Valor: {valor_grande:,}")  # Formatação com vírgulas

# Arredondamentos
preco = 123.789
print(f"Preço arredondado: R$ {round(preco, 2)}")
```

---

## 🆚 Comparação Detalhada PHP vs Python

| Operação | PHP | Python |
|----------|-----|---------|
| **Divisão** | `10 / 3` → `3.33` (float) | `10 / 3` → `3.33` (sempre float) |
| **Divisão inteira** | `intval(10/3)` | `10 // 3` |
| **Potência** | `pow(2, 3)` | `2 ** 3` |
| **Concatenação** | `$a .= $b` | `a += b` |
| **Ternário** | `$x ? $a : $b` | `a if x else b` |
| **Incremento** | `$i++` | `i += 1` |

---

## 🎯 Pontos-Chave

1. **Divisão sempre float**: `/` sempre retorna float
2. **Potência nativa**: `**` é mais limpo que `pow()`
3. **Ternário invertido**: valor primeiro, condição no meio
4. **Não há `++`**: Use `+= 1`
5. **Operadores compostos**: Idênticos ao PHP

---

## 🚀 Próxima Aula
**Aula 03 - Manipulação de Strings**

---

**Arquivo de exemplo:** [`operacoes.py`](../operacoes.py)
