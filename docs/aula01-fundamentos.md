# 📖 Aula 01 - Fundamentos do Python

## 🎯 Objetivos da Aula
- Entender print statements
- Aprender sobre variáveis sem `$`
- Conhecer os tipos primitivos
- Dominar comentários em Python

---

## 🖨️ Print Statements

### **Analogia PHP → Python:**
```php
// PHP
echo "Olá Mundo";
echo "Número: " . 42;
print("Texto");
```

```python
# Python
print("Olá Mundo")
print("Número:", 42)
print("Texto")
```

### **Características:**
- ✅ **Python**: `print()` é uma função
- ✅ **Vírgula automática**: `print("A:", valor)` adiciona espaço
- ✅ **Múltiplos valores**: `print("Nome:", nome, "Idade:", idade)`

---

## 📝 Variáveis

### **Diferenças principais:**
```php
// PHP
$nome = "João";
$idade = 25;
$ativo = true;
```

```python
# Python
nome = "João"
idade = 25
ativo = True
```

### **Regras importantes:**
- ❌ **Sem `$`** antes do nome
- ❌ **Sem `;`** no final (opcional)
- ✅ **Case sensitive**: `nome` ≠ `Nome`
- ✅ **Snake_case recomendado**: `nome_usuario`

---

## 🔢 Tipos Primitivos

### **Comparação Completa:**

| Tipo | PHP | Python | Exemplo Python |
|------|-----|--------|----------------|
| **Inteiro** | `int` | `int` | `idade = 25` |
| **Decimal** | `float` | `float` | `preco = 19.99` |
| **Texto** | `string` | `str` | `nome = "João"` |
| **Booleano** | `bool` | `bool` | `ativo = True` |
| **Nulo** | `null` | `NoneType` | `valor = None` |

### **Peculiaridades do Python:**
```python
# Booleanos com maiúscula
ativo = True    # não true
falso = False   # não false

# None com maiúscula  
vazio = None    # não null

# Verificar tipo
print(type(idade))     # <class 'int'>
print(type(preco))     # <class 'float'>
print(type(nome))      # <class 'str'>
```

---

## 💬 Comentários

### **Tipos de comentários:**
```python
# Comentário de linha única

# Comentário
# de múltiplas
# linhas

"""
Docstring - usado para documentação
de funções, classes e módulos
"""

print("Código")  # Comentário inline
```

### **Analogia PHP:**
```php
// PHP
// Comentário linha
/* Comentário
   múltiplas linhas */
# Também funciona
```

```python
# Python
# Comentário linha  
# Para múltiplas linhas
# use # em cada linha
```

---

## ✅ Exercícios Práticos

### **1. Print básico:**
```python
print("Meu primeiro programa Python!")
print("Número favorito:", 42)
print("Python", "é", "incrível!")
```

### **2. Variáveis e tipos:**
```python
# Informações pessoais
nome = "Emilio"
idade = 28
altura = 1.75
programador = True
empresa = None

# Exibir informações
print("Nome:", nome)
print("Idade:", idade, "anos")
print("Altura:", altura, "m")
print("É programador:", programador)
print("Empresa atual:", empresa)
```

### **3. Verificar tipos:**
```python
numero = 42
print("Tipo de numero:", type(numero))

texto = "Python"  
print("Tipo de texto:", type(texto))

decimal = 3.14
print("Tipo de decimal:", type(decimal))
```

---

## 🎯 Pontos-Chave para PHP Developers

1. **Sem `$`**: A maior diferença visual
2. **Maiúsculas importantes**: `True`, `False`, `None`
3. **Indentação**: Python usa espaços, não `{}`
4. **Função print()**: Não é statement como `echo`
5. **Tipagem dinâmica**: Como PHP, mas mais rigorosa

---

## 🚀 Próxima Aula
**Aula 02 - Operadores e Operações Matemáticas**

---

**Arquivo de exemplo:** [`codigo.py`](../codigo.py)
