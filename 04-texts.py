faturamento = 1000
custo = 700
lucro = faturamento - custo

# f"" operator for string interpolation
print(f"Faturamento: {faturamento}, Custo: {custo}, Lucro: {lucro}")

'''
Concatenations
# caution error-> print("Faturamento: "+ faturamento) # throws runtime error because faturamento is int
# Solution for case what you want to concatenate string with integer using str()
'''
print("Faturamento: " + str(faturamento))  # converter int para str
email = "EMAIL_falso@gmail.CoM" # diferent of "email@gmail.com"

# String methods work like objects. Familiar from javascript!
# .lower() - converts string to lowercase
# string startes in position 0
print("Email minusculo:", email.lower()) # oooooHH variables with powers of methods

# string like objects.methods. I'm familiar.
print( email.lower()   )

# find position of @ returns position(int) of @ in string
print( email.find("@") ) 
posicao_arroba = email.find("@")

# 11: 11:14 :11
print(email[posicao_arroba])

# find position of . returns position(int) of . in string
print("A posição do @ é:", posicao_arroba)

# tudo que vem antes do @
print("Tudo que vem antes do @:", email[:posicao_arroba]) 

# tudo que vem depois do @
print("Tudo que vem depois do @:", email[posicao_arroba+1:]) 

# tudo que vem entre o @ e o .
print("Tudo que vem entre o @ e o .:", email[posicao_arroba+1:email.find(".")]) 

# length of string. 
print("Tamanho do email:", len(email))  # len is built-in function

# replace - substitui uma parte da string por outra
email_trocado = email.lower().replace("gmail.com", "uerj.br") #  Wow, method chaining.
print("Email atualizado:", email_trocado)  # update email.

# specials 
print(f"Faturamento: R${faturamento:.2f}\n Custo: {custo:.2f}\n Lucro: {lucro:.2f}\n")  # format float with 2 decimal places

margem = lucro / faturamento  # margem de lucro
print(f"Margem: {margem:.1%}")  # format float with 1 decimal place

