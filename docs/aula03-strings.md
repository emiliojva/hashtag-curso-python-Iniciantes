# 📝 Aula 03 - Manipulação de Strings

## 🎯 Objetivos da Aula
- Dominar métodos de string em Python
- Entender string slicing
- Aprender F-strings para interpolação
- Comparar com manipulação de strings PHP

---

## 🔤 Métodos de String

### **Analogia PHP → Python:**
```php
// PHP - funções externas
$email = "EMAIL_falso@gmail.CoM";
$lower = strtolower($email);
$upper = strtoupper($email);
$pos = strpos($email, "@");
$replaced = str_replace("gmail", "hotmail", $email);
```

```python
# Python - métodos do objeto
email = "EMAIL_falso@gmail.CoM"
lower = email.lower()
upper = email.upper()
pos = email.find("@")
replaced = email.replace("gmail", "hotmail")
```

### **Principais métodos:**
```python
texto = "  Python Programming  "

# Transformações
texto.lower()         # "  python programming  "
texto.upper()         # "  PYTHON PROGRAMMING  "
texto.title()         # "  Python Programming  "
texto.capitalize()    # "  python programming  "

# Limpeza
texto.strip()         # "Python Programming"
texto.lstrip()        # "Python Programming  "
texto.rstrip()        # "  Python Programming"

# Busca
texto.find("Python")  # 2 (índice)
texto.count("m")      # 2 (ocorrências)

# Verificações
texto.startswith("  Py")  # True
texto.endswith("  ")      # True
texto.isdigit()           # False
texto.isalpha()           # False (tem espaços)
```

---

## ✂️ String Slicing

### **Sintaxe: `string[start:end:step]`**
```python
email = "joao@minhaempresa.com"

# Índices básicos
primeiro = email[0]        # "j"
ultimo = email[-1]         # "m"

# Slicing básico
usuario = email[:4]        # "joao"
dominio = email[5:]        # "minhaempresa.com"
arroba_ate_fim = email[4:] # "@minhaempresa.com"

# Slicing com índices
nome_parte = email[1:4]    # "oao"
servidor = email[5:17]     # "minhaempresa"

# Slicing negativo
extensao = email[-4:]      # ".com"
sem_extensao = email[:-4]  # "joao@minhaempresa"
```

### **Comparação com PHP:**
```php
// PHP
$email = "joao@empresa.com";
$usuario = substr($email, 0, 4);           // "joao"
$dominio = substr($email, 5);              // "empresa.com"
$servidor = substr($email, 5, 7);          // "empresa"
```

```python
# Python - mais intuitivo
email = "joao@empresa.com"
usuario = email[:4]                        # "joao"
dominio = email[5:]                        # "empresa.com"
servidor = email[5:12]                     # "empresa"
```

---

## 📝 F-strings (Interpolação)

### **Evolução das strings em Python:**
```python
nome = "João"
idade = 25

# Método antigo (não recomendado)
msg1 = "Nome: " + nome + ", Idade: " + str(idade)

# .format() (intermediário)
msg2 = "Nome: {}, Idade: {}".format(nome, idade)

# F-strings (recomendado - Python 3.6+)
msg3 = f"Nome: {nome}, Idade: {idade}"
```

### **Analogia PHP → Python:**
```php
// PHP
$nome = "João";
$idade = 25;
$msg = "Nome: {$nome}, Idade: {$idade}";
// ou
$msg = "Nome: $nome, Idade: $idade";
```

```python
# Python
nome = "João"
idade = 25
msg = f"Nome: {nome}, Idade: {idade}"
```

### **F-strings avançadas:**
```python
preco = 19.99
quantidade = 3

# Operações dentro da F-string
total = f"Total: R$ {preco * quantidade:.2f}"

# Formatação de números
valor = 1234.567
formatado = f"Valor: {valor:,.2f}"  # "Valor: 1,234.57"

# Expressões condicionais
nota = 8.5
resultado = f"Situação: {'Aprovado' if nota >= 7 else 'Reprovado'}"

# Chamadas de métodos
email = "JOAO@EMPRESA.COM"
msg = f"Email normalizado: {email.lower()}"
```

---

## 🎨 String Padding

### **Analogia com `str_pad()` do PHP:**
```php
// PHP
$numero = "123";
$padded = str_pad($numero, 8, "0", STR_PAD_LEFT);   // "00000123"
$right = str_pad($numero, 8, "0", STR_PAD_RIGHT);   // "12300000"
$center = str_pad($numero, 8, "-", STR_PAD_BOTH);   // "--123---"
```

```python
# Python
numero = "123"
padded = numero.rjust(8, "0")    # "00000123"
right = numero.ljust(8, "0")     # "12300000"
center = numero.center(8, "-")   # "--123---"

# Método específico para zeros
zero_filled = numero.zfill(8)    # "00000123"
```

---

## ✅ Exercícios Práticos

### **1. Processamento de email:**
```python
email = "joao@minhaempresa.com"

# Extrair informações
posicao_arroba = email.find("@")
usuario = email[:posicao_arroba]
dominio = email[posicao_arroba + 1:]
servidor = dominio.split(".")[0]
extensao = dominio.split(".")[-1]

print(f"Usuário: {usuario}")
print(f"Servidor: {servidor}")
print(f"Extensão: {extensao}")
```

### **2. Mascaramento de dados:**
```python
email = "joao@empresa.com"
posicao_arroba = email.find("@")

# Mascarar nome de usuário
usuario_original = email[:posicao_arroba]
primeira_letra = usuario_original[0]
resto_mascarado = "*" * (len(usuario_original) - 1)
email_mascarado = primeira_letra + resto_mascarado + email[posicao_arroba:]

print(f"Email mascarado: {email_mascarado}")  # "j***@empresa.com"
```

### **3. Formatação de dados:**
```python
nome = "minha empresa"
faturamento = 1234567.89

# Formatação de nome
nome_formatado = nome.title()  # "Minha Empresa"

# Formatação de valor
valor_formatado = f"R$ {faturamento:,.2f}"  # "R$ 1,234,567.89"

# Mensagem final
mensagem = f"A empresa '{nome_formatado}' teve faturamento de {valor_formatado}"
print(mensagem)
```

### **4. Validações de entrada:**
```python
def validar_email(email):
    email = email.strip().lower()
    
    # Verificações básicas
    tem_arroba = "@" in email
    tem_ponto = "." in email
    nao_vazio = len(email) > 0
    
    valido = tem_arroba and tem_ponto and nao_vazio
    return f"Email {'válido' if valido else 'inválido'}: {email}"

# Teste
emails = ["  JOAO@EMPRESA.COM  ", "teste@", "email.com", ""]
for email in emails:
    print(validar_email(email))
```

---

## 🆚 Comparação Detalhada PHP vs Python

| Operação | PHP | Python |
|----------|-----|---------|
| **Minúsculas** | `strtolower($str)` | `str.lower()` |
| **Maiúsculas** | `strtoupper($str)` | `str.upper()` |
| **Buscar posição** | `strpos($str, $needle)` | `str.find(substring)` |
| **Substituir** | `str_replace($old, $new, $str)` | `str.replace(old, new)` |
| **Substring** | `substr($str, $start, $len)` | `str[start:end]` |
| **Interpolação** | `"Olá {$nome}"` | `f"Olá {nome}"` |
| **Padding** | `str_pad($str, $len, $pad)` | `str.rjust(len, pad)` |

---

## 🎯 Pontos-Chave

1. **OOP approach**: Métodos do objeto vs funções externas
2. **Slicing poderoso**: `[start:end]` mais intuitivo que `substr()`
3. **F-strings**: Interpolação mais limpa que concatenação
4. **Imutabilidade**: Strings não mudam, métodos retornam nova string
5. **Method chaining**: `email.lower().replace().strip()`

---

## 🚀 Próxima Aula
**Aula 04 - Input do Usuário e Estruturas Condicionais**

---

**Arquivos de exemplo:** [`textos.py`](../textos.py) | [`exercicio.py`](../exercicio.py)
