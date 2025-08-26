# exercises
nome    = "Minha Empresa"
email   = "joao@minhaempresa.com"

# descubra o servidor do email
posicao_arroba = email.find("@")
print("Servidor do email:", email[posicao_arroba+1:])

# pegar o 1º nome do usuario
posicao = nome.find(" ")
nome_usuario = nome[:posicao]
print("Primeiro nome do usuario:", nome_usuario)

# construa uma mensagem: Usuario {primeiro_nome} cadastrado com sucesso com email
print(f"Usuário {nome_usuario.title()} cadastrado com sucesso com email {email.lower()}")

# construa uma mensagem: Enviamos um link de confirmação para o email {email}
nome_sem_inicial = email[1:posicao_arroba]
nome_mascarado = email[0] + ("*" * len(nome_sem_inicial)) + email[posicao_arroba:]
# Use the masked email variable instead of 'nome'
print(f"Enviamos um link de confirmação para o email {nome_mascarado.lower()}")
