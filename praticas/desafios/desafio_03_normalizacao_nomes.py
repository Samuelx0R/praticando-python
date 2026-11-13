# Desafio 03 - Normalização de Nomes
# Remove espaços extras nas pontas e deixa as iniciais maiúsculas.

# --- Entrada de dados ---
print("Insira o seu nome: ")
nome = input()

# --- Formatação ---
print(nome.title().strip())
