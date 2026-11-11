nome = input("Informe o seu nome: ") # Exibe a mensagem, espera entrada do teclado, converte para string e atribuí a entrada para a variável
print(nome)

# Ao printar variáveis, existem formas de exibi-la

nome, idade = "samuel", 21

print(nome, idade)                  # Exibe com separador ' ' (vazio/espaço)
print(nome, idade, end="...\n")     # "end" acrescenta algo ao final da saída
print(nome, idade, sep="#")         # Altera o separador