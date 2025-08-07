# 🐍 Curso Python para Iniciantes - Apoio Educacional

## 📋 Sobre o Curso

Este repositório contém material de apoio ao **"Curso Python para Iniciantes"** da [Hashtag Programação](https://www.youtube.com/watch?v=BxMtSb2w9Sk), com foco em **analogias PHP → Python** para acelerar o aprendizado.

### 👨‍🏫 Metodologia de Ensino

- **Analogias PHP ↔ Python**: Comparações diretas para facilitar a transição
- **Prática Imediata**: Cada conceito é testado com código real
- **Comentários Bilíngues**: Português + Inglês para imersão
- **Exercícios Progressivos**: Do básico ao intermediário

---

## 🎯 Conceitos Abordados

### ✅ **Fundamentos Básicos**
- [x] Print statements e output
- [x] Variáveis (sem `$` do PHP)
- [x] Tipos primitivos (int, float, str, bool, NoneType)
- [x] Comentários (`#` vs `//` do PHP)

### ✅ **Operações e Operadores**
- [x] Operadores matemáticos (+, -, *, /, %, **)
- [x] Operadores de atribuição (+=, -=, *=, /=)
- [x] Operador ternário (`"Sim" if condicao else "Não"`)

### ✅ **Manipulação de Strings**
- [x] String methods (.lower(), .upper(), .find(), .replace())
- [x] String slicing ([start:end])
- [x] F-strings (f"{variavel}")
- [x] String padding (.ljust(), .rjust(), .center(), .zfill())
- [x] Concatenação e multiplicação de strings

### 🚧 **Em Andamento**
- [ ] Input do usuário
- [ ] Estruturas condicionais (if/elif/else)
- [ ] Loops (for/while)
- [ ] Listas e dicionários
- [ ] Funções

---

## 🔄 Analogias PHP → Python

### **Sintaxe Básica**
```php
// PHP
$nome = "João";
$idade = 25;
echo "Nome: " . $nome;
```

```python
# Python
nome = "João"
idade = 25
print(f"Nome: {nome}")
```

### **Operadores**
```php
// PHP
$valor += 10;
$resultado = $condicao ? "Sim" : "Não";
$texto = str_pad("123", 5, "0", STR_PAD_LEFT);
```

```python
# Python
valor += 10
resultado = "Sim" if condicao else "Não"
texto = "123".rjust(5, "0")
```

### **Tipos de Dados**
| PHP | Python | Observação |
|-----|--------|------------|
| `null` | `None` | N maiúsculo |
| `true/false` | `True/False` | T/F maiúsculo |
| `$variavel` | `variavel` | Sem $ |
| `echo` | `print()` | Função em Python |

---

## 📁 Estrutura do Projeto

```
python/
├── README.md                 # Este arquivo
├── docs/                     # Documentação das aulas
│   ├── aula01-fundamentos.md
│   ├── aula02-operadores.md
│   └── aula03-strings.md
├── codigo.py                 # Conceitos básicos e tipos
├── operacoes.py             # Operadores e cálculos
├── textos.py                # Manipulação de strings
└── exercicio.py             # Exercícios práticos
```

---

## 🚀 Como Executar

### **No VS Code (WSL Ubuntu):**
```bash
# Terminal integrado (Ctrl + `)
python3 arquivo.py

# Ou usar o botão Play ▶️ no editor
```

### **Verificar Python:**
```bash
python3 --version
```

---

## 📚 Recursos Complementares

- **Curso Original**: [Hashtag Programação - Python para Iniciantes](https://www.youtube.com/watch?v=BxMtSb2w9Sk)
- **Documentação Python**: [docs.python.org](https://docs.python.org/pt-br/3/)
- **Comparações PHP vs Python**: Ver pasta `docs/`

---

## 🎓 Progresso do Aluno

### **Conceitos Dominados:**
- ✅ Sintaxe básica Python
- ✅ Tipos de dados primitivos
- ✅ Operadores matemáticos e de atribuição
- ✅ Manipulação básica de strings
- ✅ String slicing e methods
- ✅ F-strings e interpolação
- ✅ Operador ternário

### **Próximos Passos:**
- 🎯 Input do usuário
- 🎯 Estruturas condicionais
- 🎯 Loops e iteração
- 🎯 Estruturas de dados (listas, dicionários)

---

## 💡 Dicas de Estudo

1. **Practice First**: Execute cada exemplo antes de avançar
2. **PHP Mindset**: Use analogias para acelerar o aprendizado
3. **English Comments**: Pratique inglês técnico nos comentários
4. **Break and Build**: Quebre o código, entenda os erros, reconstrua

---

**Happy Coding! 🐍✨**

> *"A melhor forma de aprender Python é fazendo analogias com o que você já sabe."*
