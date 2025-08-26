# 🐍 Curso Python para Iniciantes - Apoio Educacional

## 📋 Sobre o Curso

Este repositório contém material de apoio ao **"Curso Python para Iniciantes"** da [Hashtag Programação](https://www.youtube.com/watch?v=BxMtSb2w9Sk), com foco em **analogias PHP → Python** para acelerar o aprendizado.

### 👨‍🏫 Metodologia de Ensino
- Analogias constantes entre PHP e Python
- Prática imediata: cada conceito é testado com código real
- Comentários bilíngues (PT/EN)
- Exercícios progressivos: do básico ao intermediário

---

## 📊 Progresso do Curso
```
Progresso: ████████░░ 75%

✅ Fundamentos       (100%)
✅ Operadores        (100%)
✅ Strings           (100%)
🚧 Input/Condicionais (0%)
📋 Loops             (0%)
📋 Estruturas        (0%)
📋 Funções           (0%)
```

---

## 📖 Índice das Aulas

### ✅ [Aula 01 - Fundamentos](docs/aula01-fundamentos.md)
- Print statements vs `echo`
- Variáveis sem `$`
- Tipos primitivos (int, float, str, bool, NoneType)
- Sistema de comentários
- Arquivo prático: [`codigo.py`](01-variables.py)

### ✅ [Aula 02 - Operadores](docs/aula02-operadores.md)
- Operadores matemáticos (+, -, *, /, //, %, **)
- Operadores de atribuição (+=, -=, *=, /=)
- Operador ternário (sintaxe diferente)
- Conversões de tipo
- Arquivo prático: [`operacoes.py`](03-basic-operations.py)

### ✅ [Aula 03 - Strings](docs/aula03-strings.md)
- Métodos de string (.lower(), .upper(), .find(), .replace())
- String slicing ([start:end])
- F-strings para interpolação
- String padding (.rjust(), .ljust(), .center())
- Arquivos práticos: [`textos.py`](04-texts.py) | [`exercicio.py`](04E-exercises.py)

### 🚧 [Aula 04 - Input e Condicionais](docs/aula04-input-condicionais.md) *(Em desenvolvimento)*
- Função `input()` vs `$_POST` do PHP
- Estruturas `if/elif/else` vs `if/elseif/else`
- Operadores de comparação
- Operadores lógicos

### 🚧 [Aula 05 - Loops](docs/aula05-loops.md) *(Planejada)*
- Loops `for` vs `foreach`
- Loop `while`
- `break` e `continue`
- Range e iteração

### 🚧 [Aula 06 - Estruturas de Dados](docs/aula06-estruturas.md) *(Planejada)*
- Listas vs arrays PHP
- Dicionários vs arrays associativos
- Métodos de listas
- Compreensão de listas

### 🚧 [Aula 07 - Funções](docs/aula07-funcoes.md) *(Planejada)*
- Definição com `def` vs `function`
- Parâmetros e argumentos
- Escopo de variáveis
- Funções lambda

---

## 🔑 Principais Diferenças PHP → Python

### Sintaxe Básica
```php
// PHP
$nome = "João";
echo "Olá, {$nome}!";
```
```python
# Python
nome = "João"
print(f"Olá, {nome}!")
```

### Operadores Especiais
| PHP | Python | Descrição |
|-----|--------|-----------|
| `$a++` | `a += 1` | Incremento |
| `$a .= $b` | `a += b` | Concatenação |
| `$a ? $b : $c` | `b if a else c` | Ternário |
| `pow($a, $b)` | `a ** b` | Potência |

### Paradigmas
- **PHP**: Funções externas + métodos
- **Python**: Métodos do objeto (mais OOP)

---

## 📚 Conceitos Abordados
- Print statements e output
- Variáveis (sem `$` do PHP)
- Tipos primitivos (int, float, str, bool, NoneType)
- Comentários (`#` vs `//` do PHP)
- Operadores matemáticos e de atribuição
- Operador ternário
- Manipulação de strings
- String slicing e methods
- F-strings e interpolação
- String padding
- Concatenação e multiplicação de strings

---

## 📁 Estrutura do Projeto
```
python/
├── README.md                 # Este arquivo
├── docs/                     # Documentação das aulas
│   ├── aula01-fundamentos.md
│   ├── aula02-operadores.md
│   ├── aula03-strings.md
│   ├── aula04-input-condicionais.md
│   ├── aula05-loops.md
│   ├── aula06-estruturas.md
│   ├── aula07-funcoes.md
├── codigo.py                 # Conceitos básicos e tipos
├── operacoes.py              # Operadores e cálculos
├── textos.py                 # Manipulação de strings
└── exercicio.py              # Exercícios práticos
```

---

## 📚 Recursos Complementares
- [Curso original - Hashtag Programação](https://www.youtube.com/watch?v=BxMtSb2w9Sk)
- [Documentação Python](https://docs.python.org/pt-br/3/)
- [Python vs PHP](https://www.php2python.com/)

---

## 💡 Dicas de Estudo
1. Execute cada exemplo antes de avançar
2. Use analogias para acelerar o aprendizado
3. Pratique inglês técnico nos comentários
4. Quebre o código, entenda os erros, reconstrua
5. Comente seu código para facilitar revisões
6. Use f-strings para interpolação: `f"Olá, {nome}"`
7. Métodos de string são muito poderosos
8. Pratique sempre, e compare com o que já conhece do PHP!

---

## 📝 Exemplos Práticos

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

**Happy Coding! 🐍✨**

> *A melhor forma de aprender Python é fazendo analogias com o que você já sabe.*

**Última atualização:** August 25, 2025
**Aluno:** Emilio
**Método:** Analogias PHP → Python


# 📚 Índice das Aulas - Curso Python para Iniciantes

## 🎯 Metodologia do Curso

Este material segue uma **abordagem comparativa PHP → Python**, facilitando a transição para desenvolvedores que já conhecem PHP/Laravel.

### **Características do método:**
- 🔄 **Analogias constantes** entre PHP e Python
- 💻 **Código prático** em cada conceito
- 🌍 **Comentários bilíngues** (PT/EN)
- 🎯 **Foco em diferenças** e semelhanças

---

## 📖 Aulas Disponíveis

### ✅ **[Aula 01 - Fundamentos](aula01-fundamentos.md)**
**Conceitos abordados:**
- Print statements vs `echo`
- Variáveis sem `$`
- Tipos primitivos (int, float, str, bool, NoneType)
- Sistema de comentários

**Arquivo prático:** [`codigo.py`](../codigo.py)

---

### ✅ **[Aula 02 - Operadores](aula02-operadores.md)**
**Conceitos abordados:**
- Operadores matemáticos (+, -, *, /, //, %, **)
- Operadores de atribuição (+=, -=, *=, /=)
- Operador ternário (sintaxe diferente)
- Conversões de tipo

**Arquivo prático:** [`operacoes.py`](../operacoes.py)

---

### ✅ **[Aula 03 - Strings](aula03-strings.md)**
**Conceitos abordados:**
- String methods (.lower(), .upper(), .find(), .replace())
- String slicing ([start:end])
- F-strings para interpolação
- String padding (.rjust(), .ljust(), .center())

**Arquivos práticos:** [`textos.py`](../textos.py) | [`exercicio.py`](../exercicio.py)

---

### 🚧 **Aula 04 - Input e Condicionais** *(Em desenvolvimento)*
**Conceitos a abordar:**
- Função `input()` vs `$_POST` do PHP
- Estruturas `if/elif/else` vs `if/elseif/else`
- Operadores de comparação
- Operadores lógicos

---

### 🚧 **Aula 05 - Loops** *(Planejada)*
**Conceitos a abordar:**
- Loops `for` vs `foreach`
- Loop `while`
- `break` e `continue`
- Range e iteração

---

### 🚧 **Aula 06 - Estruturas de Dados** *(Planejada)*
**Conceitos a abordar:**
- Listas vs arrays PHP
- Dicionários vs arrays associativos
- Métodos de listas
- Compreensão de listas

---

### 🚧 **Aula 07 - Funções** *(Planejada)*
**Conceitos a abordar:**
- Definição com `def` vs `function`
- Parâmetros e argumentos
- Escopo de variáveis
- Funções lambda

---

## 📊 Progresso Atual

```
Progresso: ████████░░ 75%

✅ Fundamentos       (100%)
✅ Operadores        (100%) 
✅ Strings           (100%)
🚧 Input/Condicionais (0%)
📋 Loops             (0%)
📋 Estruturas        (0%)
📋 Funções           (0%)
```

---

## 🔑 Principais Diferenças PHP → Python

### **Sintaxe Básica**
```php
// PHP
$nome = "João";
echo "Olá, {$nome}!";
```
```python
# Python
nome = "João"
print(f"Olá, {nome}!")
```

### **Operadores Especiais**
| PHP | Python | Descrição |
|-----|--------|-----------|
| `$a++` | `a += 1` | Incremento |
| `$a .= $b` | `a += b` | Concatenação |
| `$a ? $b : $c` | `b if a else c` | Ternário |
| `pow($a, $b)` | `a ** b` | Potência |

### **Paradigmas**
- **PHP**: Funções externas + métodos
- **Python**: Métodos do objeto (mais OOP)

---

## 🎯 Como Usar Este Material

1. **Leia a aula teórica** no arquivo `.md`
2. **Execute o código prático** no arquivo `.py`
3. **Faça as analogias** com seu conhecimento PHP
4. **Pratique os exercícios** propostos
5. **Teste variações** do código

---

## 📚 Recursos Complementares

- **Curso original**: [Hashtag - Python para Iniciantes](https://www.youtube.com/watch?v=BxMtSb2w9Sk)
- **Documentação Python**: [docs.python.org](https://docs.python.org/pt-br/3/)
- **Python vs PHP**: [php2python.com](https://www.php2python.com/)

---

**📝 Última atualização:** August 7, 2025  
**🎓 Aluno:** Emilio  
**👨‍🏫 Método:** Analogias PHP → Python
