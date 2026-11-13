 # Concatenação de string com % (Antigo e pouco usado devido a complexidade)
 # %s - string
 # %d - inteiro
 # #f - float

nome = "Samuel"
idade = 21
profissao = "Estudante"

print("Olá, me chamo %s. Eu tenho %d anos de idade e sou %s!" % (nome, idade, profissao))

# Concatenação de string com {} e .format
print("Olá, me chamo {}. Eu tenho {} anos de idade e sou {}!".format(nome, idade, profissao)) # colocar numeros dentro das chaves faz com que altere o valor seguindo o indice indicado

#.format com identificação de váriavel
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade e sou {profissao}!".format(nome = nome, idade = idade, profissao = profissao))

# fstring
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade e sou {profissao}!")

#.format com dicionário
# print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade e sou {profissao}!".format(**pessoa))