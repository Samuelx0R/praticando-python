# for em python - bom quando sabemos o numero de vezes que iremos utilizar no looping

# -----------------------------------------------------------------------

# texto = input("Informe um texto: ")
# VOGAIS = "AEIOU"

# for letra in texto:
#     if letra.upper() in VOGAIS:
#         print(letra, end="")

# print()

# -----------------------------------------------------------------------

# função range
# função built-in do python
# range(stop) -> range object
# range(start, stop[, step]) -> range object

# para mostrar os valores do range object, é necessário converter para lista utilizando list(range(stop))

# -----------------------------------------------------------------------

# print(list(range(10)))

# for numero in range(0, 21, 2):
#     print(f"{numero}", end=" ")

# -----------------------------------------------------------------------

# while (enquanto) - repete o bloco de código várias vezes quando não sabemos o número exato de vezes que o bloco deve ser excutado

# opcao = -1

# while opcao != 0:
#     opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n"))

#     if opcao == 1:
#         print("Sacando...")
#     elif opcao == 2:
#         print("Exibindo o extrato...")

# break (quebrar) - Encerra o laço
# -----------------------------------------------------------------------