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
