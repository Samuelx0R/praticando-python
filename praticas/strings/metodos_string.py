nome = "   Samuel esta fazendo testes :)  "

print(nome.upper()) # converte para maiúsculo
print(nome.lower()) # converte para minúsculo
print(nome.title()) # deixa somente a primeira letra em maíusculo
print(nome.strip()) # remove espaços em branco antes e após a string e possuí sua váriações lstrip() = esquerda (left) e rstrip() = direita (right)
print(nome.center(40, "-")) # centraliza a string var.center(quantidade de caracteres total, caractere para preencher o espaço)
print("|".join(nome)) # passa item a item concatenando separadores