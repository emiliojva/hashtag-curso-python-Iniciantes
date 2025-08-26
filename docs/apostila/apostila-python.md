 # Apostila Python para Iniciantes
 
 Bem-vindo à apostila de apoio ao curso "Python para Iniciantes"! Aqui você encontra os principais conceitos, analogias com PHP, exemplos práticos e dicas para acelerar seu aprendizado.
 
 ---
 
 ## Sumário
 - 1. Introdução ao Python
 - 2. Tipos Primitivos
 - 3. Comentários
 - 4. Operadores de atribuição
 - 5. Operador ternário
 - 6. Métodos de string
 - 7. Padding e mascaramento
 - 8. Execução no VS Code
 - 9. Analogias PHP ↔ Python
 
---

## Table of Contents / Sumário
1. Introduction to Python / Introdução ao Python
2. Primitive Types / Tipos Primitivos
3. Comments / Comentários
4. Assignment Operators / Operadores de atribuição
5. Ternary Operator / Operador ternário
6. String Methods / Métodos de string
7. Padding & Masking / Padding e mascaramento
8. Running Python in VS Code / Execução no VS Code
9. PHP ↔ Python Analogies / Analogias PHP ↔ Python
10. Practical Exercises / Exercícios práticos
11. General Tips / Dicas gerais

---

## 1. Introduction to Python / Introdução ao Python

- Easy to read, no semicolons, no `$` in variables  
    Fácil de ler, sem ponto e vírgula, sem `$` nas variáveis
- Big community and many libraries  
    Comunidade grande e muitas bibliotecas
- Indentation is required (spaces, not curly braces)  
    Indentação obrigatória (espaços, não chaves)
- Dynamic but strict typing  
    Tipagem dinâmica, mas rigorosa
- Use `print()` to show data  
    Use `print()` para mostrar dados

**Example / Exemplo:**
```python
print("Hello World")  # Olá Mundo
name = "João"
print("Name:", name)  # Nome: João
```

---

## 2. Primitive Types / Tipos Primitivos

| Type      | Python      | Example / Exemplo      |
|-----------|-------------|------------------------|
| Integer   | int         | `age = 25`             |
| Decimal   | float       | `price = 19.99`        |
| Text      | str         | `name = "João"`        |
| Boolean   | bool        | `active = True`        |
| Null      | NoneType    | `company = None`       |

**Note:** Use capital letters: `True`, `False`, `None`  
**Nota:** Use maiúsculas: `True`, `False`, `None`

**Example / Exemplo:**
```python
age = 30         # int
height = 1.75    # float
name = "Maria"   # str
active = True    # bool
empty = None     # NoneType
```

---

## 3. Comments / Comentários

- Single line: `# comment`  
    Linha única: `# comentário`
- Multiple lines: several lines starting with `#`  
    Múltiplas linhas: várias linhas começando com `#`
- Docstrings: `""" comment """` for documentation  
    Docstrings: `""" comentário """` para documentação

**Example / Exemplo:**
```python
# This is a comment
print("Hello")  # Inline comment

"""
Docstring for documentation
Docstring para documentação
"""
```

---

## 4. Assignment Operators / Operadores de atribuição

- `+=`, `-=`, `*=`, `/=`, `%=` etc.
- Example: `value += 10` (adds 10 to value)  
    Exemplo: `valor += 10` (soma 10 ao valor)

---

## 5. Ternary Operator / Operador ternário

- Syntax: `result = "Yes" if condition else "No"`  
    Sintaxe: `resultado = "Sim" if condicao else "Não"`
- PHP analogy: `$result = $condition ? "Yes" : "No";`  
    Analogia PHP: `$resultado = $condicao ? "Sim" : "Não";`

---

## 6. String Methods / Métodos de string

- `.lower()`, `.upper()`, `.title()`, `.replace()`, `.find()`
- Example: `email.lower()`, `text.replace("a", "*")`

---

## 7. Padding & Masking / Padding e mascaramento

- `.ljust()`, `.rjust()`, `.center()`, `.zfill()`
- Example: `"123".zfill(8)` → `"00000123"`
- Masking: `"*" * len(text)`

**Example / Exemplo:**
```python
number = "42"
print(number.zfill(5))        # "00042"
print(number.rjust(5, "0"))   # "00042"

name = "João"
print(name.ljust(10, "."))    # "João......"
print(name.center(10, "-"))   # "---João---"

# Email masking / Mascaramento de email
email = "joao@empresa.com"
pos = email.find("@")
masked = email[0] + ("*" * (pos-1)) + email[pos:]
print(masked)  # "j***@empresa.com"
```

---

## 8. Running Python in VS Code / Execução no VS Code

- Integrated terminal: `python3 file.py`
- Play button ▶️ in the editor
- Shortcuts: F5, Ctrl+F5, Ctrl+Shift+P → "Python: Run Python File in Terminal"
- WSL: make sure you are connected to Ubuntu

**WSL Tip / Dica WSL:**
```bash
python3 --version
sudo apt update
sudo apt install python3 python3-pip
cd /home/emilio/apps/learning/python/hashtag-curso-python-Iniciantes
python3 03-basic-operations.py
```

---

## 9. PHP ↔ Python Analogies / Analogias PHP ↔ Python

| PHP           | Python           | Note / Observação |
|---------------|------------------|-------------------|
| `$variable`   | `variable`       | No `$` / Sem $    |
| `null`        | `None`           | Capital N         |
| `true/false`  | `True/False`     | Capital T/F       |
| `echo`        | `print()`        | Function / Função |
| `str_pad()`   | `.rjust()`, `.ljust()`, `.zfill()` |
| `array()`     | `list[]`         |                   |
| `function`    | `def`            |                   |
| `? :`         | `if ... else ...`| Ternary inverted  |
| `substr()`    | `[start:end]`    | Slicing           |
| `pow()`       | `**`             | Power / Potência  |
| `$a .= $b`    | `a += b`         | Concatenation     |
| `$i++`        | `i += 1`         | Increment         |

---

## 10. Practical Exercises / Exercícios práticos

**Fundamentals / Fundamentos**
```python
print("My first Python program!")  # Meu primeiro programa Python!
name = "Emilio"
age = 28
height = 1.75
programmer = True
company = None
print("Name:", name)
print("Age:", age, "years")
print("Height:", height, "m")
print("Is programmer:", programmer)
print("Current company:", company)
```

**Operators / Operadores**
```python
revenue = 1000
cost = 700
new_sales = 300
revenue += new_sales
tax = revenue * 0.1
profit = revenue - cost - tax
margin = (profit / revenue) * 100
print(f"Total revenue: R$ {revenue}")
print(f"Profit: R$ {profit:.2f}")
print(f"Margin: {margin:.1f}%")
```

**Strings / Strings**
```python
email = "joao@minhaempresa.com"
at_pos = email.find("@")
user = email[:at_pos]
domain = email[at_pos + 1:]
server = domain.split(".")[0]
extension = domain.split(".")[-1]
print(f"User: {user}")
print(f"Server: {server}")
print(f"Extension: {extension}")
# Email masking
user_original = email[:at_pos]
first_letter = user_original[0]
masked_rest = "*" * (len(user_original) - 1)
masked_email = first_letter + masked_rest + email[at_pos:]
print(f"Masked email: {masked_email}")
# Data formatting
company_name = "minha empresa"
revenue = 1234567.89
formatted_name = company_name.title()
formatted_value = f"R$ {revenue:,.2f}"
message = f"The company '{formatted_name}' had revenue of {formatted_value}"
print(message)
# Email validation
def validate_email(email):
        email = email.strip().lower()
        has_at = "@" in email
        has_dot = "." in email
        not_empty = len(email) > 0
        valid = has_at and has_dot and not_empty
        return f"Email {'valid' if valid else 'invalid'}: {email}"
emails = ["  JOAO@EMPRESA.COM  ", "teste@", "email.com", ""]
for email in emails:
        print(validate_email(email))
```

---

## 11. General Tips / Dicas gerais

- Comment your code to help review  
    Comente seu código para facilitar revisões
- Use f-strings for interpolation: `f"Hello, {name}"`  
    Use f-strings para interpolação: `f"Olá, {nome}"`
- String methods are very powerful  
    Métodos de string são muito poderosos
- Always practice and compare with PHP  
    Pratique sempre e compare com PHP
- Test each example before moving on  
    Teste cada exemplo antes de avançar
- Break the code, understand errors, rebuild  
    Quebre o código, entenda os erros, reconstrua

---

**Happy studies! / Bons estudos!**

> Handout created by GitHub Copilot, your Python support teacher 🚀🐍

---

If you want, I can create lesson files in the docs folder too!  
Se quiser, posso criar arquivos de aula na pasta docs também!
 
 ---
 
 ## 1. Introdução ao Python
 - Linguagem de fácil leitura, sem ponto e vírgula, sem $ em variáveis
 - Comunidade enorme e muitas bibliotecas
 
 ## 2. Tipos Primitivos
 - **int**: números inteiros (ex: `42`)
 - **float**: números decimais (ex: `3.14`)
 - **str**: texto (ex: `"Python"`)
 - **bool**: verdadeiro/falso (`True`/`False`)
 - **NoneType**: ausência de valor (`None`)
 
 ### Exemplos práticos:
 ```python
 idade = 30         # int
 altura = 1.75      # float
 nome = "Maria"     # str
 ativo = True       # bool
 vazio = None       # NoneType
 ```
 
 ## 3. Comentários
 - Linha única: `# comentário`
 - Múltiplas linhas: várias linhas começando com `#`
 - Docstrings: `""" comentário """` para documentação
 
 ### Exemplos:
 ```python
 # Comentário de linha única
 print("Olá")  # Comentário ao final da linha
 
 # Comentário de múltiplas linhas
 # Linha 1
 # Linha 2
 
 """
 Docstring para documentação de funções/classes
 """
 ```
 
 ## 4. Operadores de atribuição
 - `+=`, `-=`, `*=`, `/=`, `%=` etc.
 - Exemplo: `valor += 10` (soma 10 ao valor)
 
 ## 5. Operador ternário
 - Sintaxe: `resultado = "Sim" if condicao else "Não"`
 - Analogia PHP: `$resultado = $condicao ? "Sim" : "Não";`
 
 ## 6. Métodos de string
 - `.lower()`, `.upper()`, `.title()`, `.replace()`, `.find()`
 - Exemplo: `email.lower()`, `texto.replace("a", "*")`
 
 ## 7. Padding e mascaramento
 - `.ljust()`, `.rjust()`, `.center()`, `.zfill()`
 - Exemplo: `"123".zfill(8)` → `"00000123"`
 - Mascaramento: `"*" * len(texto)`
 
 ### Exemplos práticos:
 ```python
 numero = "42"
 print(numero.zfill(5))        # "00042"
 print(numero.rjust(5, "0"))   # "00042"
 
 nome = "João"
 print(nome.ljust(10, "."))    # "João......"
 print(nome.center(10, "-"))   # "---João---"
 
 # Mascaramento de email
 email = "joao@empresa.com"
 pos = email.find("@")
 mascarado = email[0] + ("*" * (pos-1)) + email[pos:]
 print(mascarado)  # "j***@empresa.com"
 ```
 
 ## 8. Execução no VS Code
 - Terminal integrado: `python3 arquivo.py`
 - Botão "Play" ▶️ no editor
 - Atalhos: F5, Ctrl+F5, Ctrl+Shift+P → "Python: Run Python File in Terminal"
 - WSL: certifique-se de estar conectado ao Ubuntu
 
 ### Dica WSL:
 ```bash
 python3 --version
 sudo apt update
 sudo apt install python3 python3-pip
 cd /home/emilio/apps/learning/python/hashtag-curso-python-Iniciantes
 python3 03-basic-operations.py
 ```
 
 ## 9. Analogias PHP ↔ Python
 | PHP           | Python           |
 |---------------|-----------------|
 | `$variavel`   | `variavel`       |
 | `null`        | `None`           |
 | `true/false`  | `True/False`     |
 | `echo`        | `print()`        |
 | `str_pad()`   | `.rjust()`, `.ljust()`, `.zfill()` |
 | `array()`     | `list[]`         |
 | `function`    | `def`            |
 | `? :`         | `if ... else ...`|
 
 ---
 
 ## Dicas Gerais
 - Comente seu código para facilitar revisões
 - Use f-strings para interpolação: `f"Olá, {nome}"`
 - Métodos de string são muito poderosos
 - Pratique sempre, e compare com o que já conhece do PHP!
 
 ---
 
 **Bons estudos!**
 
 > Apostila criada por GitHub Copilot, seu professor de apoio Python 🚀🐍

Bem-vindo à apostila de apoio ao curso "Python para Iniciantes"! Aqui você encontra todos os conceitos estudados até agora, analogias com PHP, exemplos práticos, dicas e exercícios para acelerar seu aprendizado.

---

## Progresso do Curso
**Aulas concluídas:**
- Fundamentos do Python
- Operadores e Operações
- Manipulação de Strings
**Próximos tópicos:** Input, Condicionais, Loops, Listas, Funções

---

## Sumário
- 1. Fundamentos do Python
- 2. Tipos Primitivos
- 3. Comentários
- 4. Operadores Matemáticos e de Atribuição
- 5. Operador Ternário
- 6. Conversões e Funções Úteis
- 7. Métodos de String
- 8. String Slicing
- 9. F-strings (Interpolação)
- 10. Padding e Mascaramento
- 11. Execução no VS Code
- 12. Analogias PHP ↔ Python
- 13. Exercícios Práticos
- 14. Dicas Gerais

---

## 1. Fundamentos do Python
- Linguagem de fácil leitura, sem ponto e vírgula, sem $ em variáveis
- Comunidade enorme e muitas bibliotecas
- Indentação obrigatória (espaços, não chaves)
- Tipagem dinâmica, mas rigorosa
- Função print() para exibir dados

### Print Statements
```python
print("Olá Mundo")
print("Número:", 42)
print("Python", "é", "incrível!")
```
**Dica:** Vírgula no print adiciona espaço automaticamente.

### Variáveis
```python
nome = "João"
idade = 25
ativo = True
empresa = None
```
**Sem `$`, sem ponto e vírgula, nomes em snake_case.**

## 2. Tipos Primitivos
| Tipo        | Python      | Exemplo         |
|-------------|-------------|-----------------|
| Inteiro     | int         | `idade = 25`    |
| Decimal     | float       | `preco = 19.99` |
| Texto       | str         | `nome = "João"`|
| Booleano    | bool        | `ativo = True`  |
| Nulo        | NoneType    | `empresa = None`|
**Maiúsculas são obrigatórias:** `True`, `False`, `None`

Verificar tipo:
```python
print(type(idade))     # <class 'int'>
print(type(preco))     # <class 'float'>
print(type(nome))      # <class 'str'>
```

## 3. Comentários
- Linha única: `# comentário`
- Múltiplas linhas: várias linhas começando com `#`
- Docstrings: `""" comentário """` para documentação de funções/classes
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

## 4. Operadores Matemáticos e de Atribuição
### Operadores básicos
```python
soma = 10 + 5        # 15
subtracao = 10 - 5   # 5
multiplicacao = 10 * 5  # 50
divisao = 10 / 5     # 2.0 (sempre float)
divisao_inteira = 10 // 3  # 3
resto = 10 % 3            # 1
potencia = 2 ** 3         # 8
```
### Operadores de atribuição
```python
numero = 10
numero += 5    # numero = numero + 5
numero -= 3    # numero = numero - 3
numero *= 2    # numero = numero * 2
numero /= 4    # numero = numero / 4
numero //= 2   # numero = numero // 2
numero %= 2    # numero = numero % 2
numero **= 3   # numero = numero ** 3
```
### Concatenação de strings
```python
texto = "Olá"
texto += " Mundo"    # "Olá Mundo"
```

## 5. Operador Ternário
**Sintaxe:**
```python
resultado = "Sim" if condicao else "Não"
status = "Adulto" if idade >= 18 else "Menor"
```
**Diferença do PHP:** valor primeiro, condição no meio.
Exemplo:
```python
nota = 8.5
situacao = "Aprovado" if nota >= 7 else "Reprovado"
```

## 6. Conversões e Funções Úteis
```python
# Conversão de tipos
idade_str = "25"
idade_int = int(idade_str)
preco_str = "19.99"
preco_float = float(preco_str)
numero = 42
texto = str(numero)
# Funções built-in
numero = 123.456
arredondado = round(numero)       # 123
com_casas = round(numero, 2)      # 123.46
positivo = abs(-10)               # 10
menor = min(10, 5, 8)             # 5
maior = max(10, 5, 8)             # 10
```

## 7. Métodos de String
```python
texto = "  Python Programming  "
texto.lower()         # "  python programming  "
texto.upper()         # "  PYTHON PROGRAMMING  "
texto.title()         # "  Python Programming  "
texto.capitalize()    # "  python programming  "
texto.strip()         # "Python Programming"
texto.lstrip()        # "Python Programming  "
texto.rstrip()        # "  Python Programming"
texto.find("Python")  # 2
texto.count("m")      # 2
texto.startswith("  Py")  # True
texto.endswith("  ")      # True
texto.isdigit()           # False
texto.isalpha()           # False
```

## 8. String Slicing
```python
email = "joao@minhaempresa.com"
primeiro = email[0]        # "j"
ultimo = email[-1]         # "m"
usuario = email[:4]        # "joao"
dominio = email[5:]        # "minhaempresa.com"
arroba_ate_fim = email[4:] # "@minhaempresa.com"
nome_parte = email[1:4]    # "oao"
servidor = email[5:17]     # "minhaempresa"
extensao = email[-4:]      # ".com"
sem_extensao = email[:-4]  # "joao@minhaempresa"
```

## 9. F-strings (Interpolação)
```python
nome = "João"
idade = 25
msg1 = "Nome: " + nome + ", Idade: " + str(idade)
msg2 = "Nome: {}, Idade: {}".format(nome, idade)
msg3 = f"Nome: {nome}, Idade: {idade}"
preco = 19.99
quantidade = 3
total = f"Total: R$ {preco * quantidade:.2f}"
valor = 1234.567
formatado = f"Valor: {valor:,.2f}"
nota = 8.5
resultado = f"Situação: {'Aprovado' if nota >= 7 else 'Reprovado'}"
email = "JOAO@EMPRESA.COM"
msg = f"Email normalizado: {email.lower()}"
```

## 10. Padding e Mascaramento
```python
numero = "123"
padded = numero.rjust(8, "0")    # "00000123"
right = numero.ljust(8, "0")     # "12300000"
center = numero.center(8, "-")   # "--123---"
zero_filled = numero.zfill(8)     # "00000123"
# Mascaramento
texto = "segredo"
mascarado = "*" * len(texto)      # "*******"
```

## 11. Execução no VS Code
- Terminal integrado: `python3 arquivo.py`
- Botão "Play" ▶️ no editor
- Atalhos: F5, Ctrl+F5, Ctrl+Shift+P → "Python: Run Python File in Terminal"
- WSL: certifique-se de estar conectado ao Ubuntu

## 12. Analogias PHP ↔ Python
| PHP           | Python           | Observação |
|---------------|------------------|------------|
| `$variavel`   | `variavel`       | Sem $      |
| `null`        | `None`           | N maiúsculo|
| `true/false`  | `True/False`     | T/F maiúsculo|
| `echo`        | `print()`        | Função     |
| `str_pad()`   | `.rjust()`, `.ljust()`, `.zfill()` |
| `array()`     | `list[]`         |            |
| `function`    | `def`            |            |
| `? :`         | `if ... else ...`| Ternário invertido|
| `substr()`    | `[start:end]`    | Slicing    |
| `pow()`       | `**`             | Potência   |
| `$a .= $b`    | `a += b`         | Concatenação|
| `$i++`        | `i += 1`         | Incremento |

---

## 13. Exercícios Práticos
### Fundamentos
```python
print("Meu primeiro programa Python!")
nome = "Emilio"
idade = 28
altura = 1.75
programador = True
empresa = None
print("Nome:", nome)
print("Idade:", idade, "anos")
print("Altura:", altura, "m")
print("É programador:", programador)
print("Empresa atual:", empresa)
```
### Operadores
```python
faturamento = 1000
custo = 700
novas_vendas = 300
faturamento += novas_vendas
imposto = faturamento * 0.1
lucro = faturamento - custo - imposto
margem = (lucro / faturamento) * 100
print(f"Faturamento total: R$ {faturamento}")
print(f"Lucro: R$ {lucro:.2f}")
print(f"Margem: {margem:.1f}%")
```
### Strings
```python
email = "joao@minhaempresa.com"
posicao_arroba = email.find("@")
usuario = email[:posicao_arroba]
dominio = email[posicao_arroba + 1:]
servidor = dominio.split(".")[0]
extensao = dominio.split(".")[-1]
print(f"Usuário: {usuario}")
print(f"Servidor: {servidor}")
print(f"Extensão: {extensao}")
# Mascaramento de email
usuario_original = email[:posicao_arroba]
primeira_letra = usuario_original[0]
resto_mascarado = "*" * (len(usuario_original) - 1)
email_mascarado = primeira_letra + resto_mascarado + email[posicao_arroba:]
print(f"Email mascarado: {email_mascarado}")
# Formatação de dados
nome = "minha empresa"
faturamento = 1234567.89
nome_formatado = nome.title()
valor_formatado = f"R$ {faturamento:,.2f}"
mensagem = f"A empresa '{nome_formatado}' teve faturamento de {valor_formatado}"
print(mensagem)
# Validação de email
def validar_email(email):
    email = email.strip().lower()
    tem_arroba = "@" in email
    tem_ponto = "." in email
    nao_vazio = len(email) > 0
    valido = tem_arroba and tem_ponto and nao_vazio
    return f"Email {'válido' if valido else 'inválido'}: {email}"
emails = ["  JOAO@EMPRESA.COM  ", "teste@", "email.com", ""]
for email in emails:
    print(validar_email(email))
```

---

## 14. Dicas Gerais
- Comente seu código para facilitar revisões
- Use f-strings para interpolação: `f"Olá, {nome}"`
- Métodos de string são muito poderosos
- Pratique sempre, e compare com o que já conhece do PHP!
- Teste cada exemplo antes de avançar
- Quebre o código, entenda os erros, reconstrua

---

**Bons estudos!**

> Apostila criada por GitHub Copilot, seu professor de apoio Python 🚀🐍

---

Se quiser, posso criar arquivos de aula na pasta docs também!